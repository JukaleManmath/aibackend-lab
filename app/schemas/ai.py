from pydantic import BaseModel

# Schema models for data validation
class AiRequest(BaseModel):
    prompt: str

class AiResponse(BaseModel):
    response: str

class PasswordRequest(BaseModel):
    password: str

class PasswordResponse(BaseModel):
    suggested_password: str
    explanation: str

