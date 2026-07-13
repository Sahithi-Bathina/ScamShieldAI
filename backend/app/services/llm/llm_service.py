from groq import Groq

from app.config.settings import (
    GROQ_API_KEY,
    GROQ_MODEL,
)


class LLMService:
    """
    Service responsible for communicating with the Groq API.
    This service contains no business logic.
    """

    def __init__(self):
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set.")

        self.client = Groq(api_key=GROQ_API_KEY)

    def generate_content(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        try:
            response = self.client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                temperature=0.2,
            )

            return response.choices[0].message.content

        except Exception as e:
            raise RuntimeError(f"Groq API Error: {e}")