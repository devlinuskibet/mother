from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.health_record import HealthRecord
from app.schemas.health_schema import HealthRecordCreate, HealthRecordResponse
from app.api.auth import get_current_user # Our gatekeeper

router = APIRouter()

@router.post("/add", response_model=HealthRecordResponse)
def add_health_record(
    record: HealthRecordCreate, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Saves a new health record for the logged-in mother.
    """
    # Create the database object
    db_record = HealthRecord(
        user_email=current_user["email"], # Link to the logged-in user
        systolic_bp=record.systolic_bp,
        diastolic_bp=record.diastolic_bp,
        blood_sugar=record.blood_sugar,
        body_temp=record.body_temp,
        heart_rate=record.heart_rate,
        risk_prediction=record.risk_prediction,
        confidence_score=record.confidence_score
    )
    
    # Save to DB
    db.add(db_record)
    db.commit()
    db.refresh(db_record) # Refresh to get the generated ID and Timestamp
    
    return db_record

@router.get("/history", response_model=List[HealthRecordResponse])
def get_health_history(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Retrieves all past health records for the current user.
    """
    records = db.query(HealthRecord).filter(
        HealthRecord.user_email == current_user["email"]
    ).all()
    
    return records