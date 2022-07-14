from pydantic import BaseModel


class ResumeURL(BaseModel):
    class Url(BaseModel):
        url: str
    data: Url
    message: str