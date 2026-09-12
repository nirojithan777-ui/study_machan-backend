# tutors.py
# This file is the "Tutors" feature.
# It handles searching for tutors, looking at one tutor, updating a tutor, and finding nearby tutors.
# Many parts are still empty (TODO) and will be filled in later.
# Every line below has a simple comment explaining what it does.

from fastapi import (  # Tools from the FastAPI web framework.
    APIRouter,  # Lets us group web addresses together under one name.
    HTTPException,  # Lets us stop and send back an error message to the app.
    Query,  # Lets the web address accept extra details (like how many kilometers to search).
)
from pydantic import BaseModel  # The tool that checks and shapes data automatically.
from typing import Optional, List  # Words that describe "this can be empty" and "a list of things".

# Create a group of web addresses that all begin with /tutors.
router = APIRouter(prefix="/tutors", tags=["Tutors"])


# The shape of a "tutor profile" request, written as a data box (used when updating a tutor).
class TutorProfileCreate(BaseModel):
    bio: str  # A short "about me" story.
    hourly_rate: float  # How much the tutor charges per hour.
    subjects: List[str]  # A list of subjects the tutor teaches.
    qualifications: str  # The tutor's education or certificates.


# The shape of a "location" request, written as a data box (where the tutor is).
class LocationUpdate(BaseModel):
    lat: float  # Latitude (north/south position on a map).
    lng: float  # Longitude (east/west position on a map).


# Search for tutors, with optional filters like subject or maximum price.
@router.get("/")
def search_tutors(subject: Optional[str] = None, max_price: Optional[float] = None):
    # TODO: Query tutors from database based on filters  # This line is a note that this part is not built yet.
    return {"tutors": []}  # For now, just send back an empty list.


# Look at a single tutor's profile using their ID number.
@router.get("/{tutor_id}")
def get_tutor_by_id(tutor_id: str):
    # TODO: Fetch specific tutor profile by ID  # This line is a note that this part is not built yet.
    return {"tutor_id": tutor_id, "profile": {}}  # For now, just echo the ID and an empty profile.


# Update a tutor's profile details.
@router.put("/{tutor_id}")
def update_tutor(tutor_id: str, profile: TutorProfileCreate):
    # TODO: Update tutor profile details  # This line is a note that this part is not built yet.
    return {"message": f"Tutor {tutor_id} updated successfully", "data": profile}  # For now, just echo what was sent.


# Update where the logged-in tutor is located on the map.
@router.put("/location")
def update_tutor_location(location: LocationUpdate):
    # TODO: Update geographic coordinates for the logged-in tutor  # This line is a note that this part is not built yet.
    return {"message": "Location updated successfully", "location": location}  # For now, just echo the location.


# Find tutors that are close to a given map position within a radius.
@router.get("/nearby")
def get_nearby_tutors(lat: float = Query(...), lng: float = Query(...), radius_km: float = 10.0):
    # TODO: Calculate and return nearby tutors within the radius  # This line is a note that this part is not built yet.
    return {"lat": lat, "lng": lng, "radius_km": radius_km, "tutors": []}  # For now, just echo the position and an empty list.