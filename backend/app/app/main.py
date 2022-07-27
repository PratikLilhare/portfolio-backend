import asyncio
import aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.db import close_db_connections, init_db
from app.api.api_v1.api import api_router
from app.api.api_v1.endpoints.user import token_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
app.include_router(token_router, prefix="/token", tags=["Token"])
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )
app.add_middleware(TrustedHostMiddleware, allowed_hosts=[
                   "*"])


@app.on_event("startup")
async def startup_event():
    app.state.redis = await aioredis.from_url(
        "redis://redis", decode_responses=True
    )
    await init_db()


@app.on_event("shutdown")
async def close_redis():
    await close_db_connections()
    await app.state.redis.close()

