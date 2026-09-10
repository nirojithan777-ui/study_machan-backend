from fastapi import APIRouter

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/bookings")
def get_student_bookings():
    return {"bookings": []}

@router.get("/tutors/search")
def student_search_tutors(subject: str):
    return {"tutors": []}