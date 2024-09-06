from tortoise import Tortoise, run_async
from database.models import *
async def init():
    await Tortoise.init(
        db_url="sqlite://taskdata.db",
        # Модулем для моделей указываем __main__,
        # т.к. все модели для показа будем прописывать
        # именно тут
        modules={'models': ['__main__']},
    )
    await Tortoise.generate_schemas()
    print(await Task.all().values_list("id", "name"))
    return await Task.all().values_list("id", "name")