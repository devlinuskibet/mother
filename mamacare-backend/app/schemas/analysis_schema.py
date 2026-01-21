from pydantic import BaseModel
from typing import List

class AnalysisRequest(BaseModel):
    user_id: int
    metric: str # e.g., "bp", "glucose"

class AnalysisResult(BaseModel):
    trend: str # "increasing", "decreasing", "stable"
    slope: float
    recommendation: str
