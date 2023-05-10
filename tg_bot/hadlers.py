import types

from main import bot, dp

from aiogram.types import Message
from config import admin_id
import random

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


"""
@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, ты написал: {message.text}"

    'await bot.send_message(chat_id=message.from_user.id, text=text)'
    await message.answer(text=text)
"""




@dp.message_handler()
async def what_is_up(message: Message):

    text = message.text

    while True:
        final_answer = random.randint(0,1)
        break

    if text == "Привет" or text == "привет" or text == "Привет!":
        await bot.send_message(chat_id=admin_id, text="Привет, привет! Рад слышать!")

    if final_answer == 0 and text == "Как дела?":
        await bot.send_message(chat_id=admin_id, text="Так себе... Бывало и лучше")
    if final_answer == 1 and text == "Как дела?":
        await bot.send_message(chat_id=admin_id, text="Нормально. Бодрячком!")



