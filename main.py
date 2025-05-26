from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.db_helper import db_helper
from core.models import Base
from core.config import settings

from api.customers.views import router as customer_router
from api.products.views import router as products_router
from api.orders.views import router as orders_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(customer_router, prefix=settings.api_prefix)
app.include_router(products_router, prefix=settings.api_prefix)
app.include_router(orders_router, prefix=settings.api_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
