from fastapi import APIRouter, HTTPException, status
from app.schemas.ai import AiRequest, AiResponse, PasswordRequest, PasswordResponse
import httpx
import ast

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
        raise HTTPException(status_code=400, detail="LLM not responding or timeout exceeded")


@router.post("/password-feedback", 
             tags=["Password Feedback"], 
             status_code=status.HTTP_200_OK,
             response_model=PasswordResponse)
async def get_password_feedback(password: PasswordRequest):
    
    prompt = (
        f"Transform the password '{password.password}' to a stronger version. "
        "Return only suggestions in this format:\n"
        "Password: <new_password> (What changed: <explanation>)\n"
        "Do not return multiple paragraphs. Just the top suggestion in the specified format."
    )

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
            res = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "mistral",
                    "prompt": prompt,
                    "stream": False
                })
            try:
                data = res.json()
            except Exception as e:
                raise HTTPException(status_code=500, detail="LLM returned invalid JSON")
            if "response" not in data:
                raise HTTPException(status_code=500, detail="Malformed response from LLM")
            
            print(f"LLM response:\n{data['response']}")
            
            text = data["response"].strip()
            suggested_password = "unknown"
            explanation = "No explanation provided"

            # Handle list-style string response
            if text.startswith("[") and text.endswith("]"):
                try:
                    responses = ast.literal_eval(text)  # Converts string to actual list
                    for line in responses:
                        if line.startswith("Password:"):
                            pwd_part = line[len("Password:"):].strip()
                            if "(" in pwd_part:
                                suggested_password = pwd_part.split("(")[0].strip()
                                explanation = pwd_part.split("(", 1)[1].rstrip(")").strip()
                            else:
                                suggested_password = pwd_part
                            break
                except Exception:
                    pass
            else:
                # fallback for plain string
                for line in text.splitlines():
                    if line.startswith("Password:"):
                        pwd_part = line[len("Password:"):].strip()
                        if "(" in pwd_part:
                            suggested_password = pwd_part.split("(")[0].strip()
                            explanation = pwd_part.split("(", 1)[1].rstrip(")").strip()
                        else:
                            suggested_password = pwd_part
                        break
            
            return {
                "suggested_password": suggested_password,
                "explanation": explanation
            }

    except httpx.RequestError as e:
        raise HTTPException(status_code=400,detail="LLM not responding or timeout exceeded" )