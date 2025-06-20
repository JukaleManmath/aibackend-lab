import httpx
from sqlalchemy.orm import Session
from app.models.logs import LogTable

async def summarize_log_with_llm(raw_log: str) -> str:
    prompt = f"Summarize the following application log for readability and understanding the main issue: \n\n{raw_log}"
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
        res = await client.post("http://localhost:11434/api/generate",
                                json={
                                    "model": "mistral",
                                    "prompt": prompt,
                                    "stream": False
                                })
        return res.json()["response"]


async def process_log(raw_log: str, db: Session):
    summary = await summarize_log_with_llm(raw_log)
    log_entry = LogTable(raw_log=raw_log, summary=summary)
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return summary
