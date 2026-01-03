from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.tasks import router as tasks_router
from app.database import engine
from app.models.task import Task
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(title="Todo API", description="REST API for the Todo application", version="1.0.0")

# CORS middleware
origins = os.getenv("BACKEND_CORS_ORIGINS", ["http://localhost:3000"])
if isinstance(origins, str):
    origins = origins.replace("[", "").replace("]", "").replace("'", "").replace('"', "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tasks_router)

# Create database tables
@app.on_event("startup")
def on_startup():
    # Create all tables
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Todo API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}