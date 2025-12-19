from pydantic import BaseModel
from typing import List, Optional

class StudentProfile(BaseModel):
    name: str
    age: Optional[int] = None
    current_education: str  # e.g., "B.Tech CSE 2nd year"
    skills: List[str]
    interests: List[str]
    goals: str  # free text
    preferred_countries: Optional[List[str]] = None

class RecommendationRequest(BaseModel):
    profile: StudentProfile

class StepItem(BaseModel):
    title: str
    description: str

class CareerRecommendation(BaseModel):
    career_paths: List[str]
    learning_roadmap: List[StepItem]
    next_actions: List[StepItem]
    reasoning: str

class RecommendationResponse(BaseModel):
    recommendation: CareerRecommendation
