from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

from services import PasswordGeneratorService

from models import Number

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def main_post(number: Number):
    password = PasswordGeneratorService(number.count)
    result_password = await password.get_value()
    return JSONResponse({"result": result_password})



if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)