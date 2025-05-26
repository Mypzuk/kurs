from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .errors import ErrorTemplates
from . import functions as func

from core.db_helper import db_helper
from .schemas import CustomerCreate


async def check_customer_id(customer_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    customer = await func.get_customer(session=session, customer_id=customer_id)
    if not customer:
        return ErrorTemplates.not_found()
    return customer


async def check_customer_phone(customer_in: CustomerCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    customer = await func.get_customer(session=session, phone=customer_in.phone)
    if customer is not None:
        return ErrorTemplates.customer_already_exists()
    return customer_in