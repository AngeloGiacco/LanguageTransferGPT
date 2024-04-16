from fastapi import FastAPI, HTTPException, Depends
from services import generate_lesson
from models import User, LessonGenerationRequest, LessonResponse
from uuid import UUID
from functools import lru_cache
import config
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@lru_cache
def get_settings():
    return config.Settings()

# random data
user_data = {"angelo": User(name="angelo", email="...", id=UUID('6a132ccc-069b-4084-afb5-2024501e1aa4'), credits=3),
             "derek": User(name="derek", email="...", id=UUID('6a132cdc-069b-4084-afb5-2024501e1aa4'), credits=0)} 

@app.get('/api/health')
async def health():
    return { 'status': 'healthy' }

def get_current_user(user_name: str = "angelo") -> User:  # j simulating getting the right user
    if user_name in user_data:
        return user_data[user_name]
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/generate-lesson")
async def generate_lesson_endpoint(
    lesson_request: LessonGenerationRequest
):
    try:
        return generate_lesson(lesson_request)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))