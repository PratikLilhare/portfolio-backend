from typing import Any
from aioredis import Redis
from fastapi import APIRouter, Depends, Request

from app.api.api_v1.dependencies import get_redis, oauth2_scheme

router = APIRouter()


@router.get("/healthcheck", status_code=200)
async def test_me() -> Any:
    """
    Check status
    """
    return {"Status": "OK"}


@router.get("/security-healthcheck", status_code=200)
async def test_me(token: str = Depends(oauth2_scheme)) -> Any:
    """
    Check authentication status.
    """
    return {"Status": "OK"}


@router.get("/redis", status_code=200)
async def redis_pool(request: Request, redis: Redis = Depends(get_redis)):
    await redis.set("Redis", "OK")

    val = await redis.get("Redis")
    return {"Redis": val}
