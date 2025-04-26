from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.results.schemas import ResultSchemas
from core.models import Results
from api.responses import ResponseTemplates


async def get_result(session: AsyncSession, **kwargs):
    query = select(Results)
    for key, value in kwargs.items():
        query = query.where(getattr(Results, key) == value)
    result = await session.execute(query)
    result = result.scalars().first()
    return result


async def get_results(session):
    stmt = select(Results).order_by(Results.competition_id)
    result = await session.execute(stmt)
    results = result.scalars().all()
    result_schemas = [ResultSchemas.model_validate(result) for result in results]
    return ResponseTemplates.success(data=result_schemas)

async def create_result(result_in, session):
    result = Results(**result_in.model_dump())
    session.add(result)
    await session.commit()
    await session.refresh(result)
    return ResponseTemplates.success(data={"result_id": result.competition_id},
                                     message="Result created successfully")


async def update_result(result_in, result, session):
    for name, value in result_in:
        setattr(result, name, value)
    await session.commit()
    return ResponseTemplates.success(result_in)


async def delete_result(result_in, session):
    await session.delete(result_in)
    await session.commit()
    return ResponseTemplates.success(message=f"Result deleted")
