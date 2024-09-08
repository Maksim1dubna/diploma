import tortoise.queryset
from tortoise import run_async
from database.core import *
#cd D:\PycharmProjects\Diploma\mainProject\TortoiseOrm
#Для запуска python -m uvicorn main:app
# Swagger /docs
from fastapi import FastAPI, HTTPException, Request, Form
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
    return await Task.all()
@app.get("/main/", response_class=HTMLResponse)
async def main_page(request: Request) -> HTMLResponse:
    tasks = await main()
    print(tasks)
    return templates.TemplateResponse("main.html", {"request": request, "tasks": tasks})
@app.post('/main/create_update', response_class=HTMLResponse)
async def new_create_update(request: Request, id_cu: int = Form(...), name: str = Form(...), description: str = Form(...)):
    error = ""
    tasks = await main()
    list_id = await Task.all().values_list('id', flat=True)
    print(list_id)
    if id_cu in list_id:
        await Task.filter(id=id_cu).update(name=name, description=description)
        error = f"Задание {id_cu} ОБНОВЛЕНО"
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    else:
        await Task.create(id = id_cu, name=name, description=description)
        error = f"Задание {id_cu} СОЗДАНО"
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    return templates.TemplateResponse(
        request=request, name="main.html", context={"tasks": tasks, "error": error})

@app.post('/main/delete', response_class=HTMLResponse)
async def delete(request: Request, id_d: int = Form(...)):
    tasks = await main()
    print(tasks)
    error = ""
    list_id = await Task.all().values_list('id', flat=True)
    print(list_id)
    if id_d in list_id:
        await Task.filter(id=id_d).delete()
        error = f"Задание {id_d} УДАЛЕНО"
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    else:
        error = f"Задание {id_d} НЕ СУЩЕСТВУЕТ"
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    return templates.TemplateResponse(
        request=request, name="main.html", context={"tasks": tasks, "error": error})

if __name__ == '__main__':
    run_async(main())