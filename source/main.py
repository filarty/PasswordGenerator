from unittest import result
from fastapi import FastAPI

import uvicorn

from PasswordGenerate import Password

from services import PasswordGeneratorService

app = FastAPI()

@app.get("/")
async def index(count: int):
    result_password = await PasswordGeneratorService(count).get_value()
    return result_password


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)