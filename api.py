# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from app import run_pipeline

app = FastAPI(title="Multi-Agent AI System")

class Query(BaseModel):
    query: str

@app.post("/run")
async def run_agents(payload: Query):
    return run_pipeline(payload.query)
