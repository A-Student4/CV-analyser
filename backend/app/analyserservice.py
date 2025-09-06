from .models import AnalyseResponse, ImprovementSuggestion
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
#def get_ai_analysis():
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

    # Now steps 1 and 2: Create embeddings and store in a vector database: ChromaDB
    client = chromadb.Client()  # Initialize ChromaDB client
    collection = client.get_or_create_collection(name="cv_collection")  # Get or create a collection for CV embeddings, named "cv_collection"

    cv_chunks = []
    for chunk in cv_text.split("\n"):
        if chunk.strip():
            cv_chunks.append(chunk.strip())
    
    embeddings = genai.embed_content(model="models/text-embedding-005",
                                      content=cv_chunks,
                                      task_type="RETRIEVAL_DOCUMENT") # Create embeddings for each chunk of CV text using the specified embedding model, task type is set to "RETRIEVAL_DOCUMENT" 
    collection.add(
        documents=cv_chunks,
        embeddings=embeddings,
        ids=[f"cv_chunk_{i}" for i in range(len(cv_chunks))]  # Unique IDs for each chunk
    )
   


if __name__ == "__main__":
    """
    # Test the scraper with a sample job posting URL
    test_url = "https://job-boards.greenhouse.io/mwinternshipprogram/jobs/7998360002?utm_source=Trackr&utm_medium=tracker&utm_campaign=UK_Technology_2026&gh_src=Trackr"
    print(scrape_job_description(test_url))
    """




