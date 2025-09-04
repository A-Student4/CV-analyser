from .models import AnalyseResponse, ImprovementSuggestion
import requests
import pdfplumber
from fastapi import UploadFile
from bs4 import BeautifulSoup


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

    try:
        with pdfplumber.open(cv_file.file) as pdf:
            full_text = ""
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

    # For the purpose of this example, we will return a mock response
    mock_response = AnalyseResponse(
        match_score=90.0,
        analysis_summary="The CV is highly relevant to the job description, showcasing key skills and experiences that align well with the role.",
        suggested_improvements=[
            ImprovementSuggestion(
                original_text="Assisted in project management",
                suggested_text="Led project management efforts, resulting in a 15% increase in on-time delivery",
                improvement_reason="Highlights leadership and quantifies impact."
            ),
            ImprovementSuggestion(
                original_text="Experience with Java",
                suggested_text="Developed scalable applications using Java, improving system efficiency by 25%",
                improvement_reason="Provides specific achievements and measurable outcomes."
            )
        ]
    )

    return mock_response
    

    

   


if __name__ == "__main__":
    # Test the scraper with a sample job posting URL
    test_url = "https://job-boards.greenhouse.io/mwinternshipprogram/jobs/7998360002?utm_source=Trackr&utm_medium=tracker&utm_campaign=UK_Technology_2026&gh_src=Trackr"
    print(scrape_job_description(test_url))