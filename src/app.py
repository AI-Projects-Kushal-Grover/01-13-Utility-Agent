from pathlib import Path
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from handlers import query_handlers
from models import QueryRequest, QueryResponse

# Load environment variables from .env file
env_file = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_file)

app = FastAPI(title="Utility Agent", version="0.1.0")

@app.post("/answer")
async def answer(request: QueryRequest) -> QueryResponse:
    try:
        logging.info("Received request for answering query")
        return await query_handlers.answer_query(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
