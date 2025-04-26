from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: int


class UserCreate(BaseModel):
    phone: str
    telegram_id: str
    telegram_link: str
    first_name: str
    last_name: str
    birth_date: date
    sex: str = "M"
    weight: float
    height: float

class UserSchemas(UserCreate):
    id: int
    total_experience: float
    current_experience: float
    class Config:
        from_attributes = True