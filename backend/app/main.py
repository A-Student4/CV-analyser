from fastapi import FastAPI, UploadFile, File
from app import analyserservice
from .models import AnalyseRequest, AnalyseResponse, ImprovementSuggestion

app = FastAPI()

@app.get("/") # this is the root endpoint and it will be called when we access the root URL which is http://localhost:8000/ this root URL is also called the home page and this is the first page that will be displayed when we access the URL
def home():
    return {"Hello": "Prospero"}

@app.post("/analyse", response_model=AnalyseResponse)

def handle_analysis(request: AnalyseRequest) -> AnalyseResponse:
    # For the MVP, we imagine that a CV and job link was provided in the request
    # and we would process them to generate an analysis response.

    if request.job_link and request.cv_text:
        # Call the analyserservice to perform the analysis
        #cv_text = analyserservice.extract_text_from_cv(request.cv_file)
        job_description = analyserservice.scrape_job_description(request.job_link)

        analysis_response = analyserservice.get_ai_analysis(request.cv_text, job_description)
        return analysis_response
    
    else:
        # If either the job link or CV text is missing, we return a default response
        return AnalyseResponse(
            match_score=0.0,
            analysis_summary="Please provide a valid job link and CV text to get an analysis.",
            suggested_improvements=[]
        )

        
