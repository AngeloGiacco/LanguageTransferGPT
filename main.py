from typing import Union
from enum import Enum
from fastapi import FastAPI
from fastapi import Query
from pydantic import BaseModel
from typing_extensions import Annotated

class LevelEnum(Enum):
    completeBeginner="complete beginner"
    basic = "basic"
    intermediate = "intermediate"
    advanced = "advanced"
    expert = "expert"

class LessonGenerationRequest(BaseModel):
    username: str
    notes: Annotated[Union[str,None], Query(max_length=100)] #can be a bit more lenient on tokens
    targetLanguage: Annotated[str, Query(max_length=20)] #shouldn't be too many tokens
    nativeLanguage: Annotated[str, Query(max_length=20)] #shouldn't be too many tokens
    level : LevelEnum

app = FastAPI()

@app.post("/generate-lesson/<request>")
async def generateLesson(request: LessonGenerationRequest):
    return {"body" : "success"}