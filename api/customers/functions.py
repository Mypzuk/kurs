from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.responses import ResponseTemplates

from .schemas import CustomerSchemas

from core.models import Customers

# **kwargs позволяет искать пользователя не только по id, но и по другим параметрам. !ВАЖНО! чтоб искомый параметр был в БД!
async def get_customer(session: AsyncSession, **kwargs):
    query = select(Customers)
    for key, value in kwargs.items():
        query = query.where(getattr(Customers, key) == value)
    result = await session.execute(query)
    customer = result.scalars().first()
    return customer

async def get_customers(session: AsyncSession):
    stmt = select(Customers).order_by(Customers.customer_id)
    result = await session.execute(stmt)
    customers = result.scalars().all()
    customer_schemas = [CustomerSchemas.model_validate(customer) for customer in customers]
    return ResponseTemplates.success(data=customer_schemas)


async def create_customer(session: AsyncSession, customer_in):
    customer = Customers(**customer_in.model_dump())
    session.add(customer)
    await session.commit()
    await session.refresh(customer)
    return ResponseTemplates.success(data={"customer_id":customer.customer_id}, message="User created successfully")

async def update_customer(session: AsyncSession, customer_in, customer):
    for name, value in customer_in:
        setattr(customer, name, value)
    await session.commit()
    return ResponseTemplates.success(customer_in)

async def delete_user(session: AsyncSession, customer_in):
    await session.delete(customer_in)
    await session.commit()
    return ResponseTemplates.success(message=f"User deleted")