from fastapi import APIRouter, HTTPException
from app.schemas.ai import AiRequest, AiResponse
import httpx

router = APIRouter(prefix="/ai", tags=["LLM routes"])

@router.post("/ask", response_model=AiResponse)
async def ask_question_to_llm(prompt: AiRequest):
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client: 
            res = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "mistral",
                    "prompt": prompt.prompt,
                    "stream": False
                }
            )
            try:
                data = res.json()
            except Exception as e:
                raise HTTPException(status_code=500, detail="Invalid JSON returned from LLM")

            if "response" not in data:
                raise HTTPException(status_code=500, detail="Malformed response from LLM")

            return {"response": data["response"]}

    except httpx.RequestError as e:
        print("Exception caught:", repr(e))
        raise HTTPException(status_code=400, detail="LLM not responding or timeout exceeded")
