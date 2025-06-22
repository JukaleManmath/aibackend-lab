from pydantic import BaseModel

class LogRequest(BaseModel):
    raw_log: str

class LogResponse(BaseModel):
    summary: str

class LogChatRequest(BaseModel):
    question: str

class LogChatResponse(BaseModel):
    answer: str