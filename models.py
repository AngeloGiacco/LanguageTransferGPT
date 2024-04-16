from typing import Union
from enum import Enum
from uuid import UUID
from pydantic import BaseModel
from fastapi import Query 
from typing_extensions import Annotated

class LevelEnum(Enum):
    COMPLETE_BEGINNER = "complete beginner"
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class User(BaseModel):
    id: UUID
    name: str
    email: str
    credits: int = 0  

class LessonGenerationRequest(BaseModel):
    notes: Annotated[Union[str, None], Query(max_length=100)] 
    target_language: Annotated[str, Query(max_length=20)] 
    native_language: Annotated[str, Query(max_length=20)] 
    level: LevelEnum

    model_config = {
        "schema_extra": {
            "examples": [
                {
                    "notes": "i want a lesson about food!",
                    "target_language": "French",
                    "native_language": "English",
                    "level": LevelEnum.COMPLETE_BEGINNER 
                }
            ]
        }
    }

class LessonResponse(BaseModel):
    content: str 
    native_language: str 
    target_language: str