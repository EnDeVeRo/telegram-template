from pyrogram import Client, filters
from tortoise_models.basemodel import Admins, Scam
import re


@Client.on_message(filters.command("add", "/") & filters.private)
async def add_user(client, message):
    if len(message.text.split()) < 2:
        return await client.send_message(chat_id=message.chat.id, text="Укажите айди человека!")
    if len(message.text.split('\n')) < 2:
        return await client.send_message(chat_id=message.chat.id, text="Укажите Количество и причину")
    from_id = message.from_user.id
    user_id = re.search(r'@(\w+)', message.text)
    count, reason = message.text.split('\n')[1].split()
    if user_id:
        user_id = (await client.resolve_peer(user_id.group(1))).user_id
        if await Admins.filter(user_id=from_id).first() is not None:
            if await Scam.filter(user_id=user_id).first() is not None:
                counts = await Scam.filter(user_id=user_id).first()
                await Scam.filter(user_id=user_id).update(count_scamming=counts.count_scamming + 1)
                return await client.send_message(chat_id=message.chat.id,
                                                 text='Скамер уже в базе,добавил ему +1 к скаму')
            else:
                await Scam.create(user_id=user_id, reason=reason, count_scamming=count, date='1')
                return await client.send_message(chat_id=message.chat.id,
                                                 text='Скамер Добавлен в базу!')
        return await client.send_message(chat_id=message.chat.id,
                                         text='К сожалению у вас недостаточно прав')
    else:
        return await client.send_message(chat_id=message.chat.id, text='Ты указал не существующий никнейм!')