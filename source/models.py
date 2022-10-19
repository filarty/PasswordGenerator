from pydantic import BaseModel, validator


class Number(BaseModel):
    count: int
    
    @validator("count")
    def check_count_value(cls, v):
        if v > 60:
            raise ValueError("To many values!")
        return v