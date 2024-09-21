from pyrogram import Client, filters
from tortoise_models.basemodel import User


@Client.on_message(filters.command("update", "/") & filters.private)
async def pyrogram_update(client, message):
    if len(message.command) < 3:
        return await client.send_message(chat_id=message.chat.id, text="Необходимо указать имена.")
    old_user_name = message.command[1]
    new_user_name = message.command[2]
    if await User.filter(user_name=old_user_name).first() is None:
        return await client.send_message(chat_id=message.chat.id, text="Данного имени нет в базе данных.")
    else:
        await User.filter(user_name=old_user_name).update(user_name=new_user_name)
        return await client.send_message(chat_id=message.chat.id, text="Имя успешно изменено в базе данных.")


#                          Пример диалога с ботом
#   USER: /update
#                                           Необходимо указать имена. :BOT
#   USER: /update Ivan Anton
#                                 Имя успешно изменено в базе данных. :BOT
#   USER: /update Ivan Anton
#                                    Данного имени нет в базе данных. :BOT