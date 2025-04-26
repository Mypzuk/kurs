from datetime import date

from pydantic import BaseModel

class Competition(BaseModel):
    competition_id: int


class CompetitionCreate(BaseModel):
    title: str
    type: str
    password: str
    video_instruction: str
    start_date: date
    end_date: date
    status: str
    priority: int
    coef_m: float
    coef_f: float


class CompetitionSchemas(CompetitionCreate):
    competition_id: int
    class Config:
        from_attributes = True