from fastapi import APIRouter

from app.services.llm.gemini_service import GeminiService

router = APIRouter()

gemini = GeminiService()


@router.post("/test")
def test():

    response = gemini.generate("Say Hello")

    return {
        "response": response
    }