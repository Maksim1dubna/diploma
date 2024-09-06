import tortoise.queryset
from tortoise import run_async
from database.core import *
#cd D:\PycharmProjects\Diploma\mainProject\TortoiseOrm
#Для запуска python -m uvicorn main:app
# Swagger /docs
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database.core import *
from pydantic import BaseModel
from typing import List
from database.models import Task
import nest_asyncio
nest_asyncio.apply()
app = FastAPI()
templates = Jinja2Templates(directory="templates")
async def main():
    await init()
@app.get("/main/", response_class=HTMLResponse)
async def main_page(request: Request, ) -> HTMLResponse:
    tasks = await Tortoise.init()
    print(tasks)
    return templates.TemplateResponse(
        request=request, name="main.html", context={"tasks": tasks}
    )
if __name__ == '__main__':
    run_async(main())