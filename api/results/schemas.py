from pydantic import BaseModel

class Result(BaseModel):
    result_id: int

class ResultCreate(BaseModel):
    competition_id: int
    user_id: int
    video: str
    count: int
    points: float
    status: str

class ResultSchemas(ResultCreate):
    result_id: int

    class Config:
        from_attributes = True