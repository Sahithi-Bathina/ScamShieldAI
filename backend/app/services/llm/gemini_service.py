import google.generativeai as genai

from app.config.settings import GEMINI_API_KEY


class GeminiService:
    """
    Service responsible for communicating with the Gemini API.
    This service should contain NO business logic.
    """

    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set.")

        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash"
        )

    def generate_content(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Sends a prompt to Gemini and returns the generated text.

        Args:
            system_prompt: Instructions describing the model's role.
            user_prompt: The actual user input to analyze.

        Returns:
            Generated response as plain text.
        """

        prompt = f"""
SYSTEM INSTRUCTIONS:
{system_prompt}

USER INPUT:
{user_prompt}
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            raise Exception(f"Gemini API Error: {str(e)}")