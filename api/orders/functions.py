from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.orders.schemas import OrderSchemas
from core.models import Orders
from api.responses import ResponseTemplates


async def get_order(session: AsyncSession, **kwargs):
    query = select(Orders)
    for key, value in kwargs.items():
        query = query.where(getattr(Orders, key) == value)
    order = await session.execute(query)
    order = order.scalars().first()
    return order


async def get_orders(session):
    stmt = select(Orders).order_by(Orders.customer_id)
    order = await session.execute(stmt)
    orders = order.scalars().all()
    order_schemas = [OrderSchemas.model_validate(order) for order in orders]
    return ResponseTemplates.success(data=order_schemas)

async def create_order(order_in, session):
    order = Orders(**order_in.model_dump())
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return ResponseTemplates.success(data={"order_id": order.order_id},
                                     message="order created successfully")


async def update_order(order_in, order, session):
    for name, value in order_in:
        setattr(order, name, value)
    await session.commit()
    return ResponseTemplates.success(order_in)


async def delete_order(order_in, session):
    await session.delete(order_in)
    await session.commit()
    return ResponseTemplates.success(message=f"order deleted")
