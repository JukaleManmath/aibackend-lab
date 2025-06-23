from fastapi import FastAPI
from .database.db import engine
from .models.user import Base
from .routes.user import router as user_router
from app.routes.ai import router as ai_router
from app.routes.logs import router as log_router
from app.routes.ws_chat import router as websocket_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def welcome():
    return {"message":"AI Backend Lab is live!"}

app.include_router(user_router)
app.include_router(ai_router)
app.include_router(log_router)
app.include_router(websocket_router)