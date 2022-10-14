import re
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

from services import PasswordGeneratorService

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "count": result_password})

@app.post("/")
async def main_post():
    ...



if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)