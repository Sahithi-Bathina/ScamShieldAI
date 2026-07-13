from pathlib import Path


def load_prompt(agent_name: str) -> str:
    prompt_path = (
        Path(__file__).parent.parent
        / "prompts"
        / agent_name
        / "system_prompt.md"
    )

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()