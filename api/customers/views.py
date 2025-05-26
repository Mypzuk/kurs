from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from . import dependencies
from .schemas import CustomerSchemas, CustomerCreate
from core.db_helper import db_helper

from . import functions as func

router = APIRouter(tags=["Customers 👥"])


@router.get("/customer/{customer_id}")
async def get_customer(customer: CustomerSchemas = Depends(dependencies.check_customer_id)):
    return customer


@router.get("/customers")
async def get_customers(session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.get_customers(session=session)


@router.post("/customers")
async def create_customer(
    customer_in: CustomerCreate = Depends(dependencies.check_customer_phone),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await func.create_customer(session=session, customer_in=customer_in)


@router.put("/customer/{customer_id}")
async def update_customer(
    customer_in: CustomerCreate,
    customer=Depends(dependencies.check_customer_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await func.update_customer(
        session=session, customer_in=customer_in, customer=customer
    )


@router.delete("/customer/{customer_id}")
async def delete_customer(
    customer_in: CustomerSchemas = Depends(dependencies.check_customer_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await func.delete_user(session=session, customer_in=customer_in)
