from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .responses import ResponseTemplates
from . import functions as func

from core.db_helper import db_helper
from .schemas import UserCreate


async def check_user_id(user_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    user = await func.get_user(session=session, id=user_id)
    if not user:
        return ResponseTemplates.not_found()
    return user


async def check_user_phone(user_in: UserCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    user = await func.get_user(session=session, phone=user_in.phone)
    if user is not None:
        return ResponseTemplates.user_already_exists()
    return user_in