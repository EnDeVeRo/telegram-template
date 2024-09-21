import fastapi
import uvicorn

from pyrogram import Client
from tortoise import Tortoise
from config import ProjectConfig

from fastapi_response import fastapi_create_items, fastapi_delete_items, fastapi_update_items


app = fastapi.FastAPI()
app.include_router(fastapi_create_items.router)
app.include_router(fastapi_delete_items.router)
app.include_router(fastapi_update_items.router)


@app.on_event("startup")
async def on_startup_tortoise():
    await Tortoise.init(
        db_url=f"sqlite://{ProjectConfig.BASES_PATH}",
        modules={"models": [ProjectConfig.MODEL_PATH]}
    )
    await Tortoise.generate_schemas()


@app.on_event("startup")
async def on_startup_pyrogram():
    await Client(
        name=ProjectConfig.CLIENT_NAME,
        api_id=ProjectConfig.CLIENT_ID,
        api_hash=ProjectConfig.CLIENT_HASH,
        bot_token=ProjectConfig.CLIENT_TOKEN,
        workdir="pyrogram_session",
        plugins=dict(root="pyrogram_commands")
    ).start()


@app.on_event("shutdown")
async def on_shutdown_tortoise():
    await Tortoise.close_connections()


@app.on_event("shutdown")
async def on_shutdown_pyrogram():
    await Client.stop()


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=80, log_level="debug")