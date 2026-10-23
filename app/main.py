from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from app.config import settings

app = FastAPI(title=settings.app_name, version="0.1.0")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
    model: str | None = None


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    if not request.message or not request.message.strip():
        return ChatResponse(reply="Please provide a non-empty message.")

    if settings.openai_api_key:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=settings.openai_api_key)
            completion = client.responses.create(
                model=settings.model,
                input=[
                    {
                        "role": "user",
                        "content": request.message,
                    }
                ],
            )
            response_text = completion.output_text.strip()
            return ChatResponse(reply=response_text, model=settings.model)
        except Exception:
            return ChatResponse(
                reply=(
                    "The OpenAI API is configured but the request failed. "
                    "Please check your API key and model settings."
                ),
                model=settings.model,
            )

    return ChatResponse(
        reply=(
            "This is a starter AI agent. Add your OpenAI API key to `.env` "
            "to enable live model responses."
        ),
        model=settings.model,
    )
