from typing import List

from aioredis import Redis
from app.api.api_v1.dependencies import Github, get_redis, oauth2_scheme
from app.config import settings
from app.models import Skill, Skill_Pydantic
from app.schemas import SkillSchema, Status
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import HTTPNotFoundError

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


# Skill
@router.get("/skill", response_model=List[Skill_Pydantic], status_code=200)
async def get_skills(request: Request, redis: Redis = Depends(get_redis)):
    try:
        skills = await Skill_Pydantic.from_queryset(Skill.all())
        return skills
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/skill", response_model=Status)
async def save_skill(
    request: Request,
    project: SkillSchema,
    redis: Redis = Depends(get_redis),
    token: str = Depends(oauth2_scheme),
):
    try:
        await Skill.create(**project.dict(exclude_unset=True))
        return {"message": "Skill created successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.put(
    "/skill/{id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}}
)
async def update_skill(
    id: int,
    request: Request,
    project_schema: SkillSchema,
    redis: Redis = Depends(get_redis),
    token: str = Depends(oauth2_scheme),
):
    try:
        await Skill.filter(id=id).update(**project_schema.dict(exclude_unset=True))
        return {"message": "Skill updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.delete(
    "/skill/{id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}}
)
async def delete_skill(id: int, token: str = Depends(oauth2_scheme)):
    deleted_count = await Skill.filter(id=id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Skill {id} not found")
    return Status(message=f"Deleted skill {id}")
