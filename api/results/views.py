from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import functions as func
from . import dependencies
from core.db_helper import db_helper

from .schemas import Result, ResultCreate

router = APIRouter(tags=["Results 🎯"])

@router.get("/results/{result_id}")
async def get_result(result: Result = Depends(dependencies.check_result_id)):
    return result
@router.get("/results")
async def get_results(session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.get_results(session=session)

@router.post("/results")
async def create_result(
        result_in: ResultCreate = Depends(dependencies.check_user_competition),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await func.create_result(result_in=result_in, session=session)


@router.put("/results/{result_id}")
async def update_result(
        result_in: ResultCreate = Depends(dependencies.check_user_competition),
        result: Result = Depends(dependencies.check_result_id),
        session: AsyncSession = Depends(db_helper.session_getter)):
    return await func.update_result(result_in=result_in, result=result, session=session)

@router.delete("/results/{result_id}")
async def delete_result(
        result_in: Result = Depends(dependencies.check_result_id),
        session: AsyncSession = Depends(db_helper.session_getter)
                        ):
    return await func.delete_result(result_in=result_in, session=session)
