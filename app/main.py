from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, expense
app = FastAPI(
    title="ExpenseTrack API",
    description="A role-based expense tracking backend system",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "ExpenseTrack API is live"
    }