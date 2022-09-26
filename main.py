from aiogram.utils import executor

from config import dp, bot
import logging
import asyncio
from handlers import client, extra, callback, admin, fsmAdminMenu
from database.bot_dp import sql_creat


async def on_startup(_):
     asyncio.create_task(notifications.scheduler())


client.register_handlers_client(dp)
fsmAdminMenu.register_handlers_FSMAdmin(dp)
notifications.register_handlers_notifications(dp)
callback.register_callback_handlers(dp)
extra.register_extra_handlers(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

    
