from database.core import *
from sqlalchemy import select
# cd D:\PycharmProjects\Diploma\mainProject\SqlAlchemyOrm
#Для запуска python -m uvicorn main:app
# Swagger /docs
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database.models import Task

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/main/", response_class=HTMLResponse)
async def main_page(request: Request) -> HTMLResponse:
    tasks = session.query(Task).all()
    return templates.TemplateResponse(
        request=request, name="main.html", context={"tasks": tasks}
    )
@app.post('/main/create_update', response_class=HTMLResponse)
def new_create_update(request: Request, id_cu: int = Form(...), name: str = Form(...), description: str = Form(...)):
    error = ""
    query = select(Task.id)
    list_id = session.scalars(query).all()
    if id_cu in list_id:
        session.query(Task).filter(Task.id==id_cu).update({"name":name, "description":description})
        session.commit()
        error = f"Задание {id_cu} ОБНОВЛЕНО"
        tasks = session.query(Task).all()
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    else:
        newTask = Task(id=id_cu,
                         name=name,
                         description=description)
        session.add(newTask)
        session.commit()
        error = f"Задание {id_cu} СОЗДАНО"
        tasks = session.query(Task).all()
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    return templates.TemplateResponse(
        request=request, name="main.html", context={"tasks": tasks, "error":error})

@app.post('/main/delete', response_class=HTMLResponse)
def delete(request: Request, id_d: int = Form(...)):
    error = ""
    query = select(Task.id)
    list_id = session.scalars(query).all()
    if id_d in list_id:
        session.query(Task).filter(Task.id == id_d).delete()
        session.commit()
        error = f"Задание {id_d} УДАЛЕНО"
        tasks = session.query(Task).all()
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    else:
        error = f"Задание {id_d} НЕ СУЩЕСТВУЕТ"
        tasks = session.query(Task).all()
        return templates.TemplateResponse(
            request=request, name="main.html", context={"tasks": tasks, "error": error})
    return templates.TemplateResponse(
        request=request, name="main.html", context={"tasks": tasks, "error":error}
    )