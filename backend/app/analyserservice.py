from .models import AnalyseResponse, ImprovementSuggestion
from chromadb.utils import embedding_functions
import google.generativeai as genai
import os
import chromadb
import requests
import pdfplumber
from fastapi import UploadFile
from bs4 import BeautifulSoup
from dotenv import load_dotenv


"""
    Here, we would implement the actual logic to:
    1: Scrape the job link to get the job description
    2: Perform deep Retrieval-Augmented Generation (RAG) analysis using the CV and job information
    3: Return the full AnalyseResponse JSON object which includes match_score, analysis_summary, and suggested_improvements
"""

# Now, we will create a function that takes a URL and returns the job description text
def scrape_job_description(url: str) -> str:
    """
    Takes a URL, scrapes the webpage, and extracts the job description text.
    Returns the clean text as a string.
    """

    try:
        response = requests.get(url) # Send a GET request to the URL, which returns a Response object representing the HTML content of the job posting page
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser') 
        
        # This is a simplified example; actual implementation may vary based on the webpage structure
        job_description = soup.find('div', 'job__description body')  # Assuming the job description is within a div with class 'job-description'
        if job_description:
            return job_description.get_text(strip=True) # Extract and return the text content, stripping any extra whitespace
        else:
            return "Job description not found."
    except requests.RequestException as e:
        return f"An error occurred while fetching the job description: {e}"

def extract_text_from_cv(cv_file: UploadFile) -> str:
    """
    Takes a fastAPI UploadFile PDF file object and extracts text from it.
    and returns the extracted text as a string.
    """

    print(f"--- DEBUG: Processing file '{cv_file.filename}', content type '{cv_file.content_type}' ---")

    try:
        with pdfplumber.open(cv_file.file) as pdf:
            full_text = cv_file.filename + "\n\n"  # Start with the filename for context
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"  # Extract text from each page and add a newline for separation
        return full_text.strip()  # Return the full text, stripping any extra whitespace
    except Exception as e:
        return f"An error occurred while extracting text from the CV: {e}"
    
def get_ai_analysis(cv_text: str, job_description: str) -> AnalyseResponse:
    """
    Performs the Core RAG analysis using the CV text and job description.
    Returns a Structured AnalyseResponse object.
    """
    #1. Create embeddings for the CV text
    #2. Store the embeddings in a vector database like ChromaDB
    #3. Use the job description to query the vector database and retrieve relevant CV sections.
    #4. Construct a detailed prompt for the LLM, including the job description and retrieved CV sections.
    #5. Call the LLM API (e.g., OpenAI GPT-4).
    #6. Parse the LLM response and format it into the AnalyseResponse structure.

    # Load the Gemini API key from environment variables
    load_dotenv()  # Load environment variables from a .env file if one is present anywhere in the project directory
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=gemini_api_key)

    gemini_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=gemini_api_key, model_name="models/text-embedding-004") # Initialize the embedding function with the Gemini API key and specified model

    # Now steps 1 and 2: Create embeddings and store in a vector database: ChromaDB
    client = chromadb.Client()  # Initialize ChromaDB client
    collection = client.get_or_create_collection(name="cv_collection",
                                                 embedding_function=gemini_ef,) # Use the Gemini embedding function for creating embeddings
    
    # We will split the CV text into smaller chunks for better embedding performance and retrieval later on.
    cv_chunks = []
    for value in cv_text.split("\n"):
        if value.strip():
            cv_chunks.append(value.strip())
    
    # Create embeddings for each chunk of CV text, these embeddings will be used for similarity search later on, 
    # the purpose of the embeddings is to convert the text into a numerical format that captures its semantic meaning, allowing us to perform efficient similarity searches.
    #  Similarity searches are necessary to find the most relevant sections of the CV that match the job description.

    
    # Store the embeddings in the ChromaDB collection with unique IDs for each chunk for future retrieval  
    collection.add(
        documents=cv_chunks,
        ids=[f"cv_chunk_{i}" for i in range(len(cv_chunks))]  # Unique IDs for each chunk
    )

    # Step 3: Use the job description to query the vector database and retrieve relevant CV sections.
    results = collection.query(
        query_texts=[job_description], # Use the job description as the query text to find relevant CV sections
        n_results=5  # Retrieve the top 5 most relevant chunks, for example it could be that the top 5 chunks are the most relevant to the job description
    )

    retrieved_cv_sections = "\n---\n".join(results['documents'][0])  # Combine the retrieved CV sections into a single string, separating each section with "---" 
   
    # Step 4: Construct a detailed prompt for the LLM, including the job description and retrieved CV sections.
    prompt = f"""
    You are an expert career coach for UK university tech students. Your task is to analyze a CV against a job description and provide a match score, a summary of the analysis, and specific improvement suggestions for the CV. 

    Job Description:
    ---
    {job_description}
    ---

    RELEVANT CV SECTIONS:
    ---
    {retrieved_cv_sections}
    ---

    Based on the provided job description and the relevant sections of the CV, perform the following analysis and return your response as a valid JSON object that matches this structure:
    {{
        "match_score": Integer (0 to 100),  # An integer between 0 and 100 representing how well the CV matches the role
        "analysis_summary": str,  # A concise, encouraging summary of the CV's strengths and weaknesses for this specific role>
        "suggested_improvements": [  # A list of specific improvement suggestions for the CV
            {{
                "original_text": str,  # The original text from the CV that could be improved
                "suggested_text": str,  # The suggested improved text
                "improvement_reason": str  # A brief explanation of why the suggestion improves the CV for this role
            }},
        "closing_remarks": str  # A positive closing remark to encourage the candidate link back to the job posting and next steps  
        ]
    }}

    Focus on providing concrete, actionable improvements. Ensure the JSON is perfectly formatted.
    """

    # Step 5: Call the LLM API (e.g., Gemini or OpenAI GPT-4)
    model = genai.GenerativeModel("gemini-2.5-pro")  # Initialize the Gemini model
    response = model.generate_content(prompt)  # Generate text based on the constructed prompt

    import json
    raw_response_text = response.text
    print(f"--- DEBUG: LLM Response ---\n{raw_response_text}\n--- End of LLM Response ---")

    json_start_index = raw_response_text.find('{')
    json_end_index = raw_response_text.rfind('}') + 1 

    clean_json_string = raw_response_text[json_start_index:json_end_index]

    
    try:
        ai_response_json = json.loads(clean_json_string)  # Parse the JSON response string into a Python dictionary
        analysis_result = AnalyseResponse(**ai_response_json)  # Convert the dictionary into an AnalyseResponse object
        return analysis_result  # Return the structured AnalyseResponse object
    except json.JSONDecodeError:
        return AnalyseResponse(
            match_score=0.0,
            analysis_summary="There was an issue analyzing the response from the AI. Please try again.",
            suggested_improvements=[],
            closing_remarks="If the issue persists, please contact support."
        )



if __name__ == "__main__":
    """
    # Test the scraper with a sample job posting URL
    test_url = "https://job-boards.greenhouse.io/mwinternshipprogram/jobs/7998360002?utm_source=Trackr&utm_medium=tracker&utm_campaign=UK_Technology_2026&gh_src=Trackr"
    print(scrape_job_description(test_url))
    """




