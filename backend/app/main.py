from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from app import analyserservice
from .models import AnalyseResponse, ImprovementSuggestion

app = FastAPI()

@app.get("/") # this is the root endpoint and it will be called when we access the root URL which is http://localhost:8000/ this root URL is also called the home page and this is the first page that will be displayed when we access the URL
def home():
    return {"Hello": "Prospero"}

@app.post("/analyse", response_model=AnalyseResponse)

def handle_analysis(
    cv_file: UploadFile = File(..., description="The CV file in PDF format."),
    job_link: str = Form(..., description="The URL link to the job posting."),
    initial_prompt: Optional[str] = Form(None, description="An optional initial prompt to guide the analysis.")
) -> AnalyseResponse:
    # For the MVP, we imagine that a CV and job link was provided in the request
    # and we would process them to generate an analysis response.

    # Step 1: Extract text from the uploaded CV file
    cv_text = analyserservice.extract_text_from_cv(cv_file)

    # Step 2: Scrape the job description from the provided job link
    job_description = analyserservice.scrape_job_description(job_link)

    # Step 3: Perform the AI analysis using the extracted CV text and job description
    analysis_response = analyserservice.get_ai_analysis(
        cv_text,
        job_description,
        #initial_prompt
    )


    return analysis_response    # Return the analysis response which will be automatically converted to JSON by FastAPI
        
