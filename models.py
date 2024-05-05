from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Annotated
from annotated_types import Len
from enum import Enum


class ContinuationDifficulty(Enum):
    EASIER = 1
    SAME = 2
    HARDER = 3


class Thinking(BaseModel):
    text: str = Field(
        description="Think out loud about the grammar concepts and vocab that you want to introduce."
    )


class Introduction(BaseModel):
    text: str = Field(
        description="A brief description of the lesson introducting the topics that will be discussed. This is the first text outputted in the lesson."
    )


class Interaction(BaseModel):
    explanation: str = Field(
        "During an interaction with the user, you may want to teach some vocab, or explain a new grammar concept. You can do that here. "
    )
    question: str = Field(
        description="A question about how to say something in the foreign language. The question should be written in the native language. Make this appropriate to the level and topic requested by the user. The question should follow naturally based on the explanation field."
    )
    expected: str = Field(
        description="This is the answer in the foreign language that the student is expected to provide. Only use the foreign language."
    )


class Closing(BaseModel):
    text: str = Field(
        description="A closing message to end the lesson. Encourage the user to do another one."
    )


class Lesson(BaseModel):
    thinking: Thinking
    lesson_introduction_message: Introduction
    interactions: Annotated[list[Interaction], Len(min_length=2, max_length=5)]
    lesson_closing_message: Closing
    continuation_prompt: str = Field(
        description="a brief summary of vocab/grammar learnt in the previous lesson, so that a follow-on lesson can be generated. list vocabulary learnt concisely."
    )
