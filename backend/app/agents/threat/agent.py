import json
from pathlib import Path

from app.services.llm.llm_service import LLMService


class ThreatAgent:

    def __init__(self):
        self.llm = LLMService()

        prompt_path = (
            Path(__file__).parent.parent.parent
            / "prompts"
            / "threat"
            / "system_prompt.md"
        )

        with open(prompt_path, "r", encoding="utf-8") as file:
            self.system_prompt = file.read()

    def analyze(self, text: str) -> dict:

        response = self.llm.generate_content(
            system_prompt=self.system_prompt,
            user_prompt=text,
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            raise ValueError("Threat Agent returned invalid JSON.")