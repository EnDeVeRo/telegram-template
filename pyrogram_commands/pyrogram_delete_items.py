from pyrogram import Client, filters
from tortoise_models.basemodel import User


@Client.on_message(filters.command("delete", "/") & filters.private)
async def pyrogram_delete(client, message):
    if len(message.command) < 2:
        return await client.send_message(chat_id=message.chat.id, text="Необходимо указать имя.")
    user_name = message.command[1]
    if await User.filter(user_name=user_name).first() is None:
        return await client.send_message(chat_id=message.chat.id, text="Данного имени нет в базе данных.")
    else:
        await User.filter(user_name=user_name).delete()
        return await client.send_message(chat_id=message.chat.id, text="Имя успешно удалено из базы данных.")


#                          Пример диалога с ботом
#   USER: /delete
#                                             Необходимо указать имя. :BOT
#   USER: /delete Ivan
#                                 Имя успешно удалено из базы данных. :BOT
#   USER: /delete Ivan
#                                    Данного имени нет в базе данных. :BOT