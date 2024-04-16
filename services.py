from models import User, LessonGenerationRequest, LessonResponse

# Simulating external calls for simplicity
def _generate_lesson_content(request: LessonGenerationRequest) -> str:
    return f"Here's a lesson for {request.target_language} (Level: {request.level})..."

def generate_lesson(request: LessonGenerationRequest, user: User) -> LessonResponse:
    if user.credits <= 0:
        raise ValueError("Insufficient credits")

    # Charge the user if they have sufficient credits
    user.credits -= 1  

    content = _generate_lesson_content(request)
    return LessonResponse(
        content=content,
        native_language=request.native_language,
        target_language=request.target_language
    )