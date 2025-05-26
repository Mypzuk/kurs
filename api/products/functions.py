from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.products.schemas import ProductSchemas
from core.models import Products
from api.responses import ResponseTemplates

# **kwargs позволяет искать соревнование не только по id, но и по другим параметрам. !ВАЖНО! чтоб искомый параметр был в БД!
async def get_product(session: AsyncSession, **kwargs):
    query = select(Products)
    for key, value in kwargs.items():
        query = query.where(getattr(Products, key) == value)
    result = await session.execute(query)
    product = result.scalars().first()
    return product

async def get_products(session):
    stmt = select(Products).order_by(Products.product_id)
    result = await session.execute(stmt)
    products = result.scalars().all()
    product_schemas = [ProductSchemas.model_validate(product) for product in products]
    return ResponseTemplates.success(data=product_schemas)


async def create_product(product_in, session):
    product = Products(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return ResponseTemplates.success(data={"product_id":product.product_id}, message="Competition created successfully")

async def update_product(product_in, product, session):
    for name, value in product_in:
        setattr(product, name, value)
    await session.commit()
    return ResponseTemplates.success(product_in)

async def delete_product(product_in, session):
    await session.delete(product_in)
    await session.commit()
    return ResponseTemplates.success(message=f"product deleted")