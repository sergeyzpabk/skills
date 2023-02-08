import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.files import JSONStorage
from app.handlers.handler_exchanges_bot import register_handlers_handler
from app.config_reader import load_config


#Проверить добавление фоток в альбом через 'list'

#from app.handlers.start import register_handlers_start,start_state

logger = logging.getLogger(__name__)

FILE_DIALOG = 'dialogs.json'



async def set_commands(bot: Bot):
    commands = [
       # BotCommand(command="/start", description="Старт"),
        BotCommand(command="/menu", description="Меню"),

    ]
    await bot.set_my_commands(commands)

async def main():

    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    # Парсинг файла конфигурации
    config = load_config("config/bot.ini")

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    #dp = Dispatcher(bot, storage=MemoryStorage())
    dp = Dispatcher(bot, storage=JSONStorage('dataBase'))

    # Регистрация хэндлеров

    register_handlers_handler(dp)


    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    #await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)

    #threading.Thread(target=Posting, args=()).start()



    #threading.Thread(target=PostingCount, args=()).start()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
