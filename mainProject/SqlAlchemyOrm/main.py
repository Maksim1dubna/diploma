from database.core import *
from sqlalchemy import text
# cd D:\PycharmProjects\Diploma\mainProject\SqlAlchemyOrm
#Для запуска python -m uvicorn main:app
# Swagger /docs
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from database.models import Task

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/main/", response_class=HTMLResponse)
async def main_page(request: Request) -> HTMLResponse:
    tasks = session.query(Task).all()
    print(tasks)
    return templates.TemplateResponse(
        request=request, name="main.html", context={"tasks": tasks}
    )

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
    tasks = session.query(Task).all()
    print(tasks)
    print(type(tasks))