from typing import Any
from fastapi import APIRouter, HTTPException, Request, status

from app.schemas.resume import ResumeURL


router = APIRouter()


@router.get("/url", status_code=200, responses={200: {"model": ResumeURL}})
async def get_resume_url(request: Request) -> Any:
    """
    Get resume URL.
    """
    try:
        response = {
            "data": {
                "url": "https://drive.google.com/file/d/17fCLYT6bL32__QO_2VlF51w-QvD2Tnog/preview"
            },
            "message": "fetched successfully",
        }
        return response

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
