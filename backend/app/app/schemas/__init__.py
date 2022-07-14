from pydantic import BaseModel
from .resume import ResumeURL
from .projects import ProjectSchema


class Status(BaseModel):
    message: str