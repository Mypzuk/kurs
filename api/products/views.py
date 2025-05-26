from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from . import dependencies
from core.db_helper import db_helper

from . import functions as func
from .schemas import ProductSchemas, ProductCreate

router = APIRouter(tags=["Products 🚀"])


@router.get("/products/{product_id}")
async def get_product(product: ProductSchemas = Depends(dependencies.check_product_id)):
    return product

@router.get("/products")
async def get_products(session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.get_products(session)

@router.post("/products")
async def create_product(product_in: ProductCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.create_product(session=session, product_in=product_in)

@router.put("/products/{product_id}")
async def update_product(product_in: ProductCreate, product: ProductSchemas = Depends(dependencies.check_product_id), session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.update_product(product_in=product_in, product=product, session=session)

@router.delete("/products/{product_id}")
async def delete_product(product_in: ProductSchemas = Depends(dependencies.check_product_id), session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.delete_product(product_in=product_in, session=session)
