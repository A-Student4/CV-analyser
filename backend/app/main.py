from fastapi import FastAPI
from models import AnalyseRequest, AnalyseResponse

app = FastAPI()

@app.get("/") # this is the root endpoint and it will be called when we access the root URL which is http://localhost:8000/ this root URL is also called the home page and this is the first page that will be displayed when we access the URL
def read_root():
    return {"Hello": "Prospero"} # this will return a JSON response with a key "Hello" and value "World" on accessing the root URL

@app.post("/analyse", response_model=AnalyseResponse) 
def handle_analysis(request: AnalyseRequest) -> AnalyseResponse:
    # For the MVP, we imagine that a CV and job link was provided in the request
    # and we would process them to generate an analysis response.
    
    if request.job_link and request.cv_text:
        """
        Here, we would implement the actual logic to:
        1: Scrape the job link to get the job description
        2: Perform deep Retrieval-Augmented Generation (RAG) analysis using the CV and job information
        3: Return the full AnalyseResponse JSON object which includes match_score, analysis_summary, and suggested_improvements
        """
        pass
    else:
        # If either the job link or CV text is missing, we return a default response
        return AnalyseResponse(
            match_score=0.0,
            analysis_summary="Please a valid job link and CV text to get an analysis.",
            suggested_improvements=[]
        )


        

