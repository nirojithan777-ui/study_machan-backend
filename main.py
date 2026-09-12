# main.py
# This is the "start here" file for the whole app.
# When we run this file, it builds the web app, connects to Supabase, and turns on every feature.
# Every line below has a simple comment explaining what it does.

from typing import List, Optional  # Words that describe "a list of things" and "this can be empty".
from fastapi import (  # Tools from the FastAPI web framework.
    FastAPI,  # The tool that builds the whole web app.
    HTTPException,  # Lets us stop and send back an error message to the app.
)
from fastapi.middleware.cors import CORSMiddleware  # The tool that lets the frontend app (on a different web address) talk to us.
from pydantic import BaseModel  # The tool that checks and shapes data automatically.
from app.database import supabase  # Gets the shared connection to Supabase so we can talk to it.

# Build the web app and give it a name and a description.
app = FastAPI(
    title="StudyMachan API",  # The name of the app shown in the API list.
    description="Backend API for the StudyMachan application",  # A short sentence about what this app does.
    version="1.0.0"  # The version number of this app.
)

# Turn on CORS. This means the phone/mobile app (or website) on another web address is allowed to talk to us.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any web address to talk to us (should be limited to the real app in production).
    allow_credentials=True,  # Allow the app to send cookies or login keys with its requests.
    allow_methods=["*"],  # Allow all request types (get, post, put, ...).
    allow_headers=["*"],  # Allow all extra information headers.
)

# The shape of a "tutor profile" request, written as a data box.
class TutorProfileCreate(BaseModel):
    id: str  # The tutor's ID (same as their login ID from Supabase).
    full_name: str  # The tutor's full name.
    bio: Optional[str] = None  # A short "about me" story (can be empty).
    subjects: List[str]  # A list of subjects the tutor teaches (like English, Math).
    hourly_rate: Optional[float] = None  # How much the tutor charges per hour (can be empty).


# A simple "is the app alive?" web address.
@app.get("/")
def home():
    return {  # Send back a friendly hello message.
        "message": "StudyMachan Backend is running!",  # The text saying the app is alive.
        "status": "success"  # A word the app can check to know everything is fine.
    }


# Create a tutor profile and save it in Supabase.
@app.post("/tutors/")
def create_tutor_profile(profile: TutorProfileCreate):
    try:
        response = supabase.table("tutors").insert(profile.model_dump()).execute()  # Ask Supabase to save the tutor into the "tutors" table.
        return {"message": "Tutor profile created successfully", "data": response.data}  # Send back a happy message with the saved data.
    except Exception as e:  # If saving fails for any reason...
        raise HTTPException(status_code=400, detail=str(e))  # ...stop and send back an error message.


# Load the code of every feature (router) into the app.
import app.routers.auth as auth  # The login / signup features.
import tutors  # The tutor features (search, view tutors).
import booking  # The booking features (request a session).
import payment  # The payment features.
import student  # The student features (view bookings, search tutors).

# Turn each feature on and connect its web addresses to the app.
app.include_router(auth.router)  # Turn on the /auth addresses (signup, login, me, logout).
app.include_router(tutors.router)  # Turn on the /tutors addresses.
app.include_router(booking.router)  # Turn on the /bookings addresses.
app.include_router(payment.router)  # Turn on the /payments addresses.
app.include_router(student.router)  # Turn on the /students addresses.