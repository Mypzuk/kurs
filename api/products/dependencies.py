from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.db_helper import db_helper
from . import functions as func
from .errors import ErrorTemplates

async def check_product_id(product_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    product = await func.get_product(session=session, product_id=product_id)
    if not product:
        return ErrorTemplates.not_found()
    return product