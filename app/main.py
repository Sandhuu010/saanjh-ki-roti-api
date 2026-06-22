from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import create_db_and_tables

import app.models

from app.routers.health import router as health_router

from app.routers.auth import (
    router as auth_router
)

from app.routers.plans import (
    router as plans_router
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Saanjh Ki Roti API",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(
    health_router
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Saanjh Ki Roti API"
    }

app.include_router(
    auth_router
)

app.include_router(
    plans_router
)