from fastapi import FastAPI

import uvicorn

import asyncio

from PasswordGenerate import Password

app = FastAPI()

event_loop = asyncio.get_event_loop()

@app.get("/")
async def index(count: int):
    password = Password()
    result_password = await event_loop.run_in_executor(None, password.generate, count)
    return result_password


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)