from pydantic import BaseModel


class GetHealth(BaseModel):
    status: str
    message: str
