from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(prefix="/tutors", tags=["Tutors"])

class TutorProfileCreate(BaseModel):
    bio: str
    hourly_rate: float
    subjects: List[str]
    qualifications: str

class LocationUpdate(BaseModel):
    lat: float
    lng: float

@router.post("/")
def create_tutor_profile(profile: TutorProfileCreate):
    # TODO: Save tutor profile to Supabase database
    return {"message": "Tutor profile created successfully", "data": profile}

@router.get("/")
def search_tutors(subject: Optional[str] = None, max_price: Optional[float] = None):
    # TODO: Query tutors from database based on filters
    return {"tutors": []}

@router.get("/{tutor_id}")
def get_tutor_by_id(tutor_id: str):
    # TODO: Fetch specific tutor profile by ID
    return {"tutor_id": tutor_id, "profile": {}}

@router.put("/{tutor_id}")
def update_tutor(tutor_id: str, profile: TutorProfileCreate):
    # TODO: Update tutor profile details
    return {"message": f"Tutor {tutor_id} updated successfully", "data": profile}

@router.put("/location")
def update_tutor_location(location: LocationUpdate):
    # TODO: Update geographic coordinates for the logged-in tutor
    return {"message": "Location updated successfully", "location": location}

@router.get("/nearby")
def get_nearby_tutors(lat: float = Query(...), lng: float = Query(...), radius_km: float = 10.0):
    # TODO: Calculate and return nearby tutors within the radius
    return {"lat": lat, "lng": lng, "radius_km": radius_km, "tutors": []}