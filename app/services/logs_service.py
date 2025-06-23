import httpx
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.logs import LogTable
from app.vectorstore.embedding_utils import query_logs_from_chroma
import json

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

async def semantic_search_logs(query: str):
    return query_logs_from_chroma(query)

async def answer_log_question(question: str) -> str:
    top_responses = query_logs_from_chroma(question)
    formatted_logs = "\n\n".join([f"Log: {log['raw_log']}\nSummary: {log['summary']}" for log in top_responses])
    
    prompt = f"""
            You are a genius Log Analyzer.

            Based on the following logs:
            {formatted_logs}

            Answer this user question: "{question}"

            Respond in the format:
            answer: <your concise answer here>
                """
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
            response = await client.post("http://localhost:11434/api/generate",
                                 json={
                                     "model": "mistral",
                                     "prompt": prompt,
                                     "stream": True
                                 })
            
            final_text = ""
            async for line in response.aiter_lines():
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    token = data.get("response") or data.get("answer") or ""
                    final_text += token
                except json.JSONDecodeError:
                    continue

            cleaned = final_text.replace("answer:", "", 1).strip()
            return cleaned
    except:
        raise HTTPException(status_code=400, detail= "LLM is not responding")