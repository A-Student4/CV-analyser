from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from app import analyserservice
from .models import AnalyseResponse, ImprovementSuggestion

app = FastAPI()

# Addition OF middleware to handle CORS (Cross-Origin Resource Sharing) issues
app.add_middleware(
    CORSMiddleware, # tHIS line ADDS THE CORS MIDDLEWARE TO THE FASTAPI APPLICATION, which is necessary to allow requests from different origins (e.g., if your frontend is hosted on a different domain than your backend)
    allow_origins=["*"],  # Allows all origins, which means any domain can make requests to this API
    allow_credentials=True,  # Allows cookies and authentication headers to be included in requests
    allow_methods=["*"],  # Allows all methods so that GET, POST, PUT, DELETE, etc. requests are permitted
    allow_headers=["*"],  # Allows all headers
)



@app.get("/") # this is the root endpoint and it will be called when we access the root URL which is http://localhost:8000/ this root URL is also called the home page and this is the first page that will be displayed when we access the URL
def home():
    return {"Hello": "Prospero"}

@app.post("/analyse", response_model=AnalyseResponse)

async def handle_analysis(
    cv_file: UploadFile = File(...),
    job_link: str = Form(...),
    initial_prompt: Optional[str] = Form(None)
) -> AnalyseResponse:
    try:
        # For the MVP, we imagine that a CV and job link was provided in the request
        # and we would process them to generate an analysis response.7

        # Step 1: Extract text from the uploaded CV file
        cv_text = analyserservice.extract_text_from_cv(cv_file)

        # Step 2: Scrape the job description from the provided job link
        job_description = analyserservice.scrape_job_description(job_link)

        # Step 3: Perform the AI analysis using the extracted CV text and job description
        analysis_response = analyserservice.get_ai_analysis(
            cv_text,
            job_description,
            initial_prompt
        )

        return analysis_response    # Return the analysis response which will be automatically converted to JSON by FastAPI
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

