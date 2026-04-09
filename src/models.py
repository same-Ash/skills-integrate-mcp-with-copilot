"""
Data models for activities and participants
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class ActivitySchema(BaseModel):
    """Activity model schema"""
    name: str
    description: str
    schedule: str
    max_participants: int
    participants: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Chess Club",
                "description": "Learn strategies and compete in chess tournaments",
                "schedule": "Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 12,
                "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
            }
        }


class ActivityUpdate(BaseModel):
    """Activity update model"""
    name: Optional[str] = None
    description: Optional[str] = None
    schedule: Optional[str] = None
    max_participants: Optional[int] = None


class SignupRequest(BaseModel):
    """Signup request model"""
    email: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "student@mergington.edu"
            }
        }
