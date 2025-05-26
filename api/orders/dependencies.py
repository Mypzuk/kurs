from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.db_helper import db_helper
from . import functions as func
from .errors import ErrorTemplates
from .schemas import OrderCreate

from api.products.dependencies import check_product_id
from api.customers.dependencies import check_customer_id


async def check_order_id(order_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    order = await func.get_order(session=session, order_id=order_id)
    if not order:
        return ErrorTemplates.not_found()
    return order


async def check_customer_product(order_in: OrderCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    # result = await check_result_id(result_id=result_in.id, session=session)
    # product = await check_product_id(product_id=order_in.product_id, session=session)
    customer = await check_customer_id(customer_id=order_in.customer_id, session=session)
    return order_in