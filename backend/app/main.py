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
        # Mock response simulating analysis
        mock_response = AnalyseResponse(
            match_score=85.0,
            analysis_summary="The CV matches well with the job description, highlighting relevant skills and experiences.",
            suggested_improvements=[
                ImprovementSuggestion(
                    original_text="Managed a team of 5",
                    suggested_text="Led a team of 5 to successfully complete projects on time",
                    improvement_reason="Provides more context and impact of the leadership role."
                ),
                ImprovementSuggestion(
                    original_text="Worked on Python projects",
                    suggested_text="Developed and maintained Python applications, improving performance by 20%",
                    improvement_reason="Quantifies the contribution and adds a measurable outcome."
                )
            ]
        )
        
        return mock_response
    
    else:
        # If either the job link or CV text is missing, we return a default response
        return AnalyseResponse(
            match_score=0.0,
            analysis_summary="Please provide a valid job link and CV text to get an analysis.",
            suggested_improvements=[]
        )

        
