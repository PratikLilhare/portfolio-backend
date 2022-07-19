from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    test,
    resume,
    projects,
    user
)

api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["Test"])
api_router.include_router(resume.router, prefix="/resume", tags=["Resume"])
api_router.include_router(
    projects.router, prefix="/project", tags=["Project"])
api_router.include_router(user.router, prefix="/user", tags=["User"])
