from pydantic import BaseModel


class Payload(BaseModel):
    key: str
    val: str
