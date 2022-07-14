from aioredis import Redis
from app.api.api_v1.dependencies import Github, get_redis
from fastapi import APIRouter, Depends, Request


router = APIRouter()

### Personal Project API

@router.get("/get_avatar_url", status_code=200)
async def get_repos(request: Request, redis: Redis = Depends(get_redis)):
    url = await redis.get("avatar_url")

    response = {
        "data": {
            "url": url
        },
        "message": "fetched successfully",
    }

    if not url:
        git_api = Github()
        url = await git_api.get_avatar_url()
        await redis.set("avatar_url", url)

        response["data"]["url"] = url
        return response
    else:
        return response

