from fastapi import HTTPException


# Класс для создания стандартных ответов
class ErrorTemplates:

    @staticmethod
    def not_found(message: str = f"Продукт не найден"):
        raise HTTPException(status_code=404, detail={"message": message})
