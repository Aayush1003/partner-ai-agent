import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    app_name: str = "partner-ai-agent"
    openai_api_key: str | None = None
    model: str = "gpt-4o-mini"


settings = Settings(
    openai_api_key=os.getenv("OPENAI_API_KEY") or None,
    model=os.getenv("MODEL") or "gpt-4o-mini",
)
