from typing import Any
from aioredis import Redis
from fastapi import APIRouter, Depends, Request

from app.api.api_v1.dependencies import get_redis

router = APIRouter()


@router.get("/healthcheck", status_code=200)
async def test_me() -> Any:
    """
    Test router endpoint.
    """
    return {"Service": "OK"}


@router.get("/redis", status_code=200)
async def redis_pool(request: Request, redis: Redis = Depends(get_redis)):
    await redis.set("Redis", "OK")

    val = await redis.get("Redis")
    return {"Redis": val}
