from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import functions as func
from . import dependencies
from core.db_helper import db_helper

from .schemas import OrderSchemas, OrderCreate

router = APIRouter(tags=["Orders 🎯"])

@router.get("/orders/{order_id}")
async def get_order(order: OrderSchemas = Depends(dependencies.check_order_id)):
    return order

@router.get("/orders")
async def get_orders(session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.get_orders(session=session)

@router.post("/orders")
async def create_order(
        order_in: OrderCreate = Depends(dependencies.check_customer_product),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await func.create_order(order_in=order_in, session=session)


@router.put("/orders/{order_id}")
async def update_order(
        order_in: OrderCreate = Depends(dependencies.check_customer_product),
        order: OrderSchemas = Depends(dependencies.check_order_id),
        session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.update_order(order_in=order_in, order=order, session=session)

@router.delete("/orders/{order_id}")
async def delete_order(
        order_in: OrderSchemas = Depends(dependencies.check_order_id),
        session: AsyncSession = Depends(db_helper.session_getter) ):
    return await func.delete_order(order_in=order_in, session=session)
