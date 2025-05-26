
from fastapi import HTTPException


# Класс для создания стандартных ответов
class ErrorTemplates:

    @staticmethod
    def customer_already_exists(message: str = "Пользователь уже зарегестрирован"):
        raise HTTPException(
            status_code=404,
            detail={"message": message}
        )


    @staticmethod
    def not_found(message: str = f"Пользователь не найден"):
        raise HTTPException(
            status_code=404,
            detail={"message": message}
        )
