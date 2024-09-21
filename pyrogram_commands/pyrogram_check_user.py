from pyrogram import Client, filters
from tortoise_models.basemodel import Admins, Scam
import re

@Client.on_message(filters.command("check", "/") & filters.private)
async def check_user(client, message):
    if len(message.text.split()) < 2:
        return await client.send_message(chat_id=message.chat.id, text="Укажите айди человека!")
    user_id = re.search(r'@(\w+)', message.text)
    if user_id:
        user_id = (await client.resolve_peer(user_id.group(1))).user_id
        if await Scam.filter(user_id=user_id).first() is not None:
            message_send = '''
            🕹Ник: {}
            🆔Id: {}.
            💾Ищем по базам
            Найдено!
            '''
            nickname = await client.get_users(user_ids=user_id)
            return await client.send_message(chat_id=message.chat.id, text=message_send.format(
                nickname.username, nickname.id
            ))
        return await client.send_message(chat_id=message.chat.id, text='Кажется его нет в скам базе!')
