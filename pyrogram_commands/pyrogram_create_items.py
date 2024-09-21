from pyrogram import Client, filters
from tortoise_models.basemodel import User


@Client.on_message(filters.command("start", "/") & filters.private)
async def pyrogram_create(client, message):
    if await User.filter(user_id=message.from_user.id).first() is None:
        await User.create(user_id=message.from_user.id)
    return await client.send_message(chat_id=message.chat.id, text="Привет тебе помогут тут антискамеры!")