# Definition of the pydantic models used in the application
from fastapi import FastAPI, Form, UploadFile, File
from pydantic import BaseModel #  Pydantic is a data validation and settings management library, we import BaseModel to create data models
from typing import List, Optional # Typing is a standard library module for type hints in Python and we import List and Optional for type annotations

"""
this model defines the shape of the JSON data that will be sent to the backend
when a user makes an analysis POST request to the /analyse endpoint from the frontend
class AnalyseRequest(BaseModel):
"""
class AnalyseRequest(BaseModel):
    #cv_file: UploadFile = File(...)  # Expecting a file upload for the CV, File(...) indicates that this field is required
    cv_text: str = Form(...)  # Expecting CV text as a string, Form(...) indicates that this field is required
    job_link: str = Form(...)  # Expecting a job link as a string, Form(...) indicates that this field is required
    initial_prompt: str = Form(None)  # Optional initial prompt for the analysis, default is None


"""
the below models defines the shape of the JSON data that will be sent back to the frontend
when the backend responds to an analysis request made to the /analyse endpoint
"""
class ImprovementSuggestion(BaseModel):
    original_text: str 
    suggested_text: str 
    improvement_reason: str

class AnalyseResponse(BaseModel):
    match_score: float
    analysis_summary: str 
    suggested_improvements: List[ImprovementSuggestion]