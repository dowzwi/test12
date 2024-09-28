from aiogram import types, Dispatcher
import os
from buttons import start, info
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f"Добро пожаловать!\n"
                                                              f"Введите /info для более подробной информации!",
                           reply_markup=start)


async def info_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f'Это теллеграм бот нашего магазина!\n'
                                                              f'Тут вы можете приобрести товар!\n',
                           reply_markup=info)

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])