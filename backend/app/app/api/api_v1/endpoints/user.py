from aioredis import Redis
from app.api.api_v1.dependencies import Github, get_redis
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.config import settings


router = APIRouter()
token_router = APIRouter()

USER_ID = settings.USER_ID
USER_SECRET = settings.USER_SECRET


@token_router.post("/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not form_data.username == USER_ID:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    if not form_data.password == USER_SECRET:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    return {"access_token": USER_SECRET, "token_type": "bearer"}


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

