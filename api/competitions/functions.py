from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.competitions.schemas import CompetitionSchemas, CompetitionCreate
from core.models import Competitions
from api.responses import ResponseTemplates

# **kwargs позволяет искать соревнование не только по id, но и по другим параметрам. !ВАЖНО! чтоб искомый параметр был в БД!
async def get_competition(session: AsyncSession, **kwargs):
    query = select(Competitions)
    for key, value in kwargs.items():
        query = query.where(getattr(Competitions, key) == value)
    result = await session.execute(query)
    competition = result.scalars().first()
    return competition

async def get_competitions(session):
    stmt = select(Competitions).order_by(Competitions.competition_id)
    result = await session.execute(stmt)
    competitions = result.scalars().all()
    competition_schemas = [CompetitionSchemas.model_validate(user) for user in competitions]
    return ResponseTemplates.success(data=competition_schemas)


async def create_competition(competition_in, session):
    competition = Competitions(**competition_in.model_dump())
    session.add(competition)
    await session.commit()
    await session.refresh(competition)
    return ResponseTemplates.success(data={"competition_id":competition.competition_id}, message="Competition created successfully")

async def update_competition(competition_in, competition, session):
    for name, value in competition_in:
        setattr(competition, name, value)
    await session.commit()
    return ResponseTemplates.success(competition_in)

async def delete_competition(competition_in, session):
    await session.delete(competition_in)
    await session.commit()
    return ResponseTemplates.success(message=f"Competition deleted")