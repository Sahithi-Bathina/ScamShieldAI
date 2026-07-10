from pathlib import Path

from app.services.llm.gemini_service import GeminiService


class ThreatAgent:

    def __init__(self):
        self.gemini = GeminiService()

        prompt_path = (
            Path(__file__).parent.parent.parent
            / "prompts"
            / "threat"
            / "system_prompt.md"
        )

        with open(prompt_path, "r", encoding="utf-8") as file:
            self.system_prompt = file.read()

    def analyze(self, text: str) -> str:
        return self.gemini.generate_content(
            system_prompt=self.system_prompt,
            user_prompt=text,
        )