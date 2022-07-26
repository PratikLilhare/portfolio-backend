from pydantic import BaseModel
from .resume import ResumeURL
from .projects import ProjectSchema
from .user import (
    Skill_Queryset,
    SkillSchema,
    ExperienceSchema,
    GetExperienceSchema,
    Skill_Pydantic,
    Experience_Pydantic,
    Experience_Queryset,
)


class Status(BaseModel):
    message: str
