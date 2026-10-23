# partner-ai-agent

A starter AI agent project built with FastAPI and OpenAI-compatible APIs.

## Features
- Health check endpoint
- Simple chat endpoint
- Optional OpenAI integration when `OPENAI_API_KEY` is configured
- Easy local development setup

## Quick start

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment settings:
   ```bash
   cp .env.example .env
   ```

4. Start the app:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open API docs:
   - http://localhost:8000/docs

## API endpoints
- `GET /health` - server status
- `POST /api/chat` - send a message to the agent

## Example request
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello! Tell me about this AI agent."}'
```
