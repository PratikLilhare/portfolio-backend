from app.config import settings
from tortoise import Tortoise


TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init_db() -> None:
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={'models': ['app.models']},
    )
    await Tortoise.generate_schemas()
    

async def close_db_connections() -> None:
    await Tortoise.close_connections()


Tortoise.init_models(['app.models'], 'models')