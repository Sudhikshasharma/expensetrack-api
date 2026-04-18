

from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, expense
from app.routes import auth, users

app = FastAPI(
    title="ExpenseTrack API",
    description="Role-based Expense Tracker REST API built with FastAPI and PostgreSQL",
    version="1.0.0"
)

# Register all routes
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "ExpenseTrack API is live"
    }