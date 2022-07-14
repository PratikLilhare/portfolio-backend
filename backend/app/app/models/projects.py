from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Project(Model):
    name = fields.TextField()
    description = fields.TextField()
    url = fields.CharField(max_length=255, required=False, null=True)
    image_url = fields.CharField(max_length=255, required=False, null=True)
    languages = fields.JSONField(required=False, null=True)

    def __str__(self):
        return self.name


Project_Pydantic = pydantic_model_creator(Project, name="Project")