# Telegram Template
**Telegram Template - это пример создания бота для Telegram, который использует библиотеку Pyrogram для взаимодействия с Telegram API, фреймворк FastAPI для создания API и базу данных через Tortoise-ORM.**

## Используемые библиотеки
```
fastapi=0.95.0
uvicorn~=0.21.1
Pyrogram~=2.0.102
TgCrypto~=1.2.5
tortoise-orm~=0.19.3
requests~=2.28.2
```

## Установка и запуск
1. **Устанавливаем GIT если не установлен.**

2. **Создаем новый проект в своем редакторе кода.**

3. **Клонируем проект:**
 > ```git clone https://gitlab.com/xxxevexxx/telegram-template.git```

4. **Устанавливаем зависимости:**
 > Poetry - `poetry install`
 > 
 > Venv - `pip install -r requirements.txt`

5. **Получаем CLIENT_TOKEN:**
 > https://t.me/BotFather

6. **Получить CLIENT_ID/HASH:**
 > https://blog.lavhost.ml/telegram-api

7. **Корректируем файл config.py:**

```
CLIENT_TOKEN = "YourTelegramToken"
CLIENT_HASH = "YourTelegramHash"
CLIENT_ID = 000000
```

9. **Запуск:**
 > Poetry - `poetry run main.py`
 > 
 > Venv - `python main.py`

### P.S Буду благодарен за любую обратную связь и ваши предложения по коду.
  
### Связь со мной:
- [x] [Telegram](https://t.me/xxevex)
- [x] [LolzTeam](https://lolz.live/members/3852486/)
- [x] [Vkontakte](https://vk.com/allohadance61)