from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas.logs import LogRequest, LogResponse, LogChatRequest, LogChatResponse
from app.database.db import get_db
from app.services.logs_service import process_log ,semantic_search_logs, answer_log_question
from app.vectorstore.embedding_utils import add_log_to_chroma



router = APIRouter(prefix="/logs", tags=["Log routes"])

@router.post("/", status_code=status.HTTP_202_ACCEPTED, response_model=LogResponse)
async def summarize_log(request: LogRequest, db: Session = Depends(get_db)):
    summary = await process_log(request.raw_log, db)
    add_log_to_chroma(raw_log=request.raw_log , summary=summary)
    return {"summary": summary}

@router.get("/search")
async def search_relavant_logs(q: str):
    results = await semantic_search_logs(q)
    return results

@router.post("/chat", response_model=LogChatResponse)
async def chat_with_llm_on_logs(question: LogChatRequest):
    answer = await answer_log_question(question.question)
    return {"answer": answer}