from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import uuid4
from enum import Enum

app = FastAPI(title="Candidate Management API", version="1.0.0")

class CandidateStatus(str, Enum):
    applied = "applied"
    interview = "interview"
    selected = "selected"
    rejected = "rejected"

candidates_db: dict = {}

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    skill: str
    status: CandidateStatus = CandidateStatus.applied

class StatusUpdate(BaseModel):
    status: CandidateStatus

class CandidateResponse(BaseModel):
    id: str
    name: str
    email: str
    skill: str
    status: CandidateStatus

@app.post("/candidates", response_model=CandidateResponse, status_code=201)
def create_candidate(candidate: CandidateCreate):
    candidate_id = str(uuid4())
    record = {
        "id": candidate_id,
        "name": candidate.name,
        "email": candidate.email,
        "skill": candidate.skill,
        "status": candidate.status,
    }
    candidates_db[candidate_id] = record
    return record

@app.get("/candidates", response_model=list[CandidateResponse])
def get_candidates(status: Optional[CandidateStatus] = Query(None)):
    results = list(candidates_db.values())
    if status:
        results = [c for c in results if c["status"] == status]
    return results

@app.put("/candidates/{candidate_id}/status", response_model=CandidateResponse)
def update_status(candidate_id: str, body: StatusUpdate):
    if candidate_id not in candidates_db:
        raise HTTPException(status_code=404, detail="Candidate not found")
    candidates_db[candidate_id]["status"] = body.status
    return candidates_db[candidate_id]