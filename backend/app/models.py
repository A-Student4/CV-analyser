# Definition of the pydantic models used in the application

from pydantic import BaseModel #  Pydantic is a data validation and settings management library, we import BaseModel to create data models
from typing import List, Optional # Typing is a standard library module for type hints in Python and we import List and Optional for type annotations

"""
this model defines the shape of the JSON data that will be sent to the backend
when a user makes an analysis POST request to the /analyse endpoint from the frontend
class AnalyseRequest(BaseModel):
"""
class AnalyseRequest(BaseModel):
    cv_text: str
    job_link: Optional[str] = None
    initial_prompt: Optional[str] = None


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