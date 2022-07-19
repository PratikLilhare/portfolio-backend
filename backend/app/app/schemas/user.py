from typing import Optional
from pydantic import BaseModel

from app.models.user import SkillType


class SkillSchema(BaseModel):
    name: Optional[str]
    proficency: Optional[int]
    type: Optional[SkillType]
