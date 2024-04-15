from typing import Union
from enum import Enum
from uuid import UUID
from fastapi import FastAPI,Query, HTTPException
from pydantic import BaseModel
from typing_extensions import Annotated

userCredits = {"angelo":2,"derek":0}

class LevelEnum(Enum):
    completeBeginner="complete beginner"
    basic = "basic"
    intermediate = "intermediate"
    advanced = "advanced"
    expert = "expert"

class LessonGenerationRequest(BaseModel):
    notes: Annotated[Union[str,None], Query(max_length=100)] #can be a bit more lenient on tokens
    targetLanguage: Annotated[str, Query(max_length=20)] #shouldn't be too many tokens
    nativeLanguage: Annotated[str, Query(max_length=20)] #shouldn't be too many tokens
    level : LevelEnum

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "notes": "i want a lesson about food!",
                    "targetLanguage": "French",
                    "nativeLanguage": "English",
                    "level": "complete beginner",
                }
            ]
        }
    }

class User(BaseModel):
    id : UUID
    name : str
    email : str

class LessonResponse(BaseModel):
    content: str 
    nativeLanguage: str 
    targetLanguage: str

app = FastAPI()

@app.post("/generate-lesson/<request>")
async def generateLesson(lessonRequest: LessonGenerationRequest, user : User) -> LessonResponse:
    if userCredits[user.name] > 0:
        return {"content" : "success", "nativeLanguage":"English", "targetLanguage":"French"}
    else:
        raise HTTPException(status_code=403, detail="credits ran out")