# Dockerfile for MCP server (src layout)
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

CMD ["sh", "-c", "uvicorn src.api:app --host 0.0.0.0 --port $PORT"]
