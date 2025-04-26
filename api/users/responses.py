from pydantic import BaseModel
from typing import TypeVar, Generic, Optional
from fastapi import HTTPException

# Определяем общий тип данных для ответа
T = TypeVar('T')


# Базовая модель ответа
class APIResponse(BaseModel, Generic[T]):
    status: str
    message: str
    data: Optional[T] = None


# Класс для создания стандартных ответов
class ResponseTemplates:
    @staticmethod
    def success(data: Optional[T] = None, message: str = "Operation successful"):
        return APIResponse(
            status="success",
            message=message,
            data=data
        )

    @staticmethod
    def user_already_exists(message: str = "This user is already registered"):
        raise HTTPException(
            status_code=404,
            detail={"message": message}
        )



    @staticmethod
    def not_found(message: str = f"User not found"):
        raise HTTPException(
            status_code=404,
            detail={"message": message}
        )
