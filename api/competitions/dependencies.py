from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.db_helper import db_helper
from . import functions as func
from .errors import ErrorTemplates

async def check_competition_id(competition_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    competition = await func.get_competition(session=session, competition_id=competition_id)
    if not competition:
        return ErrorTemplates.not_found()
    return competition