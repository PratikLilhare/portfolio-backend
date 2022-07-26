from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from app.models import Experience, Skill, SkillType

from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.pydantic import pydantic_queryset_creator


class SkillSchema(BaseModel):
    name: Optional[str]
    proficency: Optional[int]
    type: Optional[SkillType]


class ExperienceSchema(BaseModel):
    company: Optional[str]
    start: Optional[date]
    end: Optional[date]
    skill: Optional[list]
    description: Optional[str]

class GetExperienceSchema(BaseModel):
    skills: List[SkillSchema]


Skill_Pydantic = pydantic_model_creator(Skill, name="Skill")
Skill_Queryset = pydantic_queryset_creator(Skill)

Experience_Pydantic = pydantic_model_creator(Experience, name="Experience", exclude_readonly=True)
Experience_Queryset = pydantic_queryset_creator(Experience)