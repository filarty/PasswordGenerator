from pydantic import BaseModel


class Number(BaseModel):
    count: int