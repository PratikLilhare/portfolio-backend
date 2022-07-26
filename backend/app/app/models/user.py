from enum import Enum
from tortoise.models import Model
from tortoise import fields


class SkillType(str, Enum):
    BACKEND = "BACKEND"
    FRONTEND = "FRONTEND"
    DEVOPS = "DEVOPS"
    OTHER = "OTHER"


class Skill(Model):
    name = fields.CharField(max_length=20)
    proficiency = fields.IntField(min=0, max=100, required=False, default=0)
    type = fields.CharEnumField(SkillType, default=SkillType.OTHER)


class Experience(Model):
    start = fields.DateField()
    end = fields.DateField(required=False, null=True)
    company = fields.CharField(max_length=20)
    skills = fields.ManyToManyField("models.Skill", related_name="skills", on_delete=fields.CASCADE)
    description = fields.TextField()

    class Meta:
        ordering = ["-start"]

