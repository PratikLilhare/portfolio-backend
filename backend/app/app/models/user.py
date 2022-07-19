from enum import Enum
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class SkillType(str, Enum):
    BACKEND = "BACKEND"
    FRONTEND = "FRONTEND"
    DEVOPS = "DEVOPS"
    OTHER = "OTHER"

class Skill(Model):
    name = fields.CharField(max_length=20)
    proficiency = fields.IntField(min=0, max=100, required=False, default=0)
    type = fields.CharEnumField(SkillType, default=SkillType.OTHER)


Skill_Pydantic = pydantic_model_creator(Skill, name="Skill")
