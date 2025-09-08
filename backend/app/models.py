# Definition of the pydantic models used in the application
from fastapi import FastAPI, Form, UploadFile, File
from pydantic import BaseModel #  Pydantic is a data validation and settings management library, we import BaseModel to create data models
from typing import List, Optional # Typing is a standard library module for type hints in Python and we import List and Optional for type annotations

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
    closing_remarks: str
    