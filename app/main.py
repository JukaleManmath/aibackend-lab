from fastapi import FastAPI
from .database.db import engine
from .models.user import Base
from .routes.user import router as user_router
from app.routes.ai import router as ai_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def welcome():
    return {"message":"AI Backend Lab is live!"}

app.include_router(user_router)
app.include_router(ai_router)