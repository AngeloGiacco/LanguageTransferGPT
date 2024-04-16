from fastapi import FastAPI, HTTPException, Depends
from services import generate_lesson
from models import User, LessonGenerationRequest, LessonResponse
from uuid import UUID

app = FastAPI()

# random data
user_data = {"angelo": User(name="angelo", email="...", id=UUID('6a132ccc-069b-4084-afb5-2024501e1aa4'), credits=3),
             "derek": User(name="derek", email="...", id=UUID('6a132cdc-069b-4084-afb5-2024501e1aa4'), credits=0)} 

def get_current_user(user_name: str) -> User:  # j simulating getting the right user
    if user_name in user_data:
        return user_data[user_name]
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/generate-lesson")  # Adjust path if needed
async def generate_lesson_endpoint(
    lesson_request: LessonGenerationRequest, 
    user: User = Depends(get_current_user)
) -> LessonResponse:
    try:
        return generate_lesson(lesson_request, user)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))