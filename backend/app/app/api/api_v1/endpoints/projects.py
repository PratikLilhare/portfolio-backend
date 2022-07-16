import json
from typing import List

from aioredis import Redis
from app.api.api_v1.dependencies import Github, get_redis, oauth2_scheme
from app.models import Project, Project_Pydantic
from app.schemas import ProjectSchema, Status
from fastapi import APIRouter, Depends, HTTPException, Request, status
from tortoise.contrib.fastapi import HTTPNotFoundError


router = APIRouter()

# Personal Project API


@router.get("/get_personal_projects", status_code=200)
async def get_repos(request: Request, redis: Redis = Depends(get_redis)):
    projects = await redis.get("projects")

    if not projects:
        git_api = Github()
        projects = await git_api.get_projects()
        await redis.setex("projects", value=json.dumps(projects), time=60*60)

        return {"projects": projects}
    else:
        return {"projects": json.loads(projects)}


# Organizational Project API

@router.get("/", response_model=List[Project_Pydantic], status_code=200)
async def get_projects(request: Request, redis: Redis = Depends(get_redis)):
    try:
        projects = await Project_Pydantic.from_queryset(Project.all())
        return projects
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/", response_model=Status)
async def save_projects(
    request: Request, project: ProjectSchema, redis: Redis = Depends(get_redis), token: str = Depends(oauth2_scheme)
):
    try:
        await Project.create(**project.dict(exclude_unset=True))
        return {"message": "Project created successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put("/{id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def update_projects(
    id: int, request: Request, project_schema: ProjectSchema, redis: Redis = Depends(get_redis), token: str = Depends(oauth2_scheme)
):
    try:
        await Project.filter(id=id).update(**project_schema.dict(exclude_unset=True))
        return {"message": "Project updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/{id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(id: int, token: str = Depends(oauth2_scheme)):
    deleted_count = await Project.filter(id=id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Project {id} not found")
    return Status(message=f"Deleted project {id}")
