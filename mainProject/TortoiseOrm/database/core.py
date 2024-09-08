from tortoise import Tortoise, run_async
from database.models import *
async def init():
    tortoise_config = {
        'connections': {
            'default': 'sqlite://taskdata.db',
        },
        'apps': {
            'models': {
                'models': ['main'],
                'default_connection': 'default',
            }
        }
    }
    await Tortoise.init(
        # Модулем для моделей указываем __main__,
        # т.к. все модели для показа будем прописывать
        # именно тут
        config=tortoise_config,
        modules={'models': ['__main__']},
    )
    await Tortoise.generate_schemas()



    # tortoise_config = {
    #     "connections": {"default": "sqlite://taskdata.db"},
    #     "apps": {
    #         "pnwapi": {
    #             "models": ["database.models"],
    #             "default_connection": "default",
    #         }
    #     },
    #     "use_tz": False,
    #     "timezone": "UTC",
    # }