from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Input: What React sends to save a record
class HealthRecordCreate(BaseModel):
    systolic_bp: int
    diastolic_bp: int
    blood_sugar: float
    body_temp: float
    heart_rate: int
    # We might optionally send the risk if calculated on the client, 
    # but usually the backend calculates it. For now, we allow passing it.
    risk_prediction: str
    confidence_score: float

# Output: What React receives when asking for history
class HealthRecordResponse(HealthRecordCreate):
    id: int
    user_email: str
    timestamp: datetime

    class Config:
        from_attributes = True