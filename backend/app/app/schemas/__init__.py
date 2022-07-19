from pydantic import BaseModel
from .resume import ResumeURL
from .projects import ProjectSchema
from .user import SkillSchema


class Status(BaseModel):
    message: str
