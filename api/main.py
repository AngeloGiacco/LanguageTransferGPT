from fastapi import FastAPI, HTTPException, Depends
from services import generate_lesson, generate_answer
from models import LessonGenerationRequest, LessonResponse, QuestionRequest, QuestionResponse
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

@app.get('/api/v1/health')
async def health():
    return { 'status': 'healthy' }


@app.post("/api/v1/generate-lesson")
async def generate_lesson_endpoint(
    lesson_request: LessonGenerationRequest
) -> LessonResponse:
    try:
        return generate_lesson(lesson_request)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    
@app.post("/api/v1/answer-question")
async def generate_answer_endpoint(
    question: QuestionRequest
) -> QuestionResponse:
    try:
        return generate_answer(question)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))