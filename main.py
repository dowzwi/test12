import logging
from aiogram.utils import executor
from buttons import start_test
from config import bot, dp, staff
from Handlers import commands, fsm_store, send_products, order_products
from db import db_main


async def on_startup(_):
    for i in staff:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start_test)
        await db_main.sql_create()


commands.register_commands(dp)
fsm_store.register_store(dp)
send_products.register_send_products_handler(dp)
order_products.register_order_handler(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)