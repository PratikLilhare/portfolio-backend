from typing import Optional
from pydantic import BaseModel, Json


class ProjectSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    url: Optional[str]
    image_url: Optional[str]
    languages: Optional[Json]