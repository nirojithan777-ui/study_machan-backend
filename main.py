import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_PUBLISHABLE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI(
    title="StudyMachan API",
    description="Backend API for the StudyMachan application",
    version="1.0.0"
)

class TutorProfileCreate(BaseModel):
    id: str  # Matches auth.users UUID from Supabase Auth
    full_name: str
    bio: Optional[str] = None
    subjects: List[str]
    hourly_rate: Optional[float] = None

@app.get("/")
def home():
    return {
        "message": "StudyMachan Backend is running!",
        "status": "success"
    }

@app.post("/tutors/")
def create_tutor_profile(profile: TutorProfileCreate):
    try:
        response = supabase.table("tutors").insert(profile.model_dump()).execute()
        return {"message": "Tutor profile created successfully", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

from auth import router as auth_router

app.include_router(auth_router)

import auth
import tutors
import booking
import payment
import student

app.include_router(auth.router)
app.include_router(tutors.router)
app.include_router(booking.router)
app.include_router(payment.router)
app.include_router(student.router)