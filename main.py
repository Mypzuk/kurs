from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.db_helper import db_helper
from core.models import Base
from core.config import settings

from api.users.views import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix=settings.api_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
