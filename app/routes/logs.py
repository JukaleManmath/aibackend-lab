from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas.logs import LogRequest, LogResponse
from app.database.db import get_db
from app.services.logs_service import process_log



router = APIRouter(prefix="/logs", tags=["Log routes"])

@router.post("/", status_code=status.HTTP_202_ACCEPTED, response_model=LogResponse)
async def summarize_log(request: LogRequest, db: Session = Depends(get_db)):
    summary = await process_log(request.raw_log, db)
    return {"summary": summary}