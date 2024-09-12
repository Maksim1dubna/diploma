from tortoise import Tortoise
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