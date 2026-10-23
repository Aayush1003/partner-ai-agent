import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "partner-ai-agent"
    openai_api_key: str | None = None
    model: str = "gpt-4o-mini"


settings = Settings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("MODEL", "gpt-4o-mini"),
)
