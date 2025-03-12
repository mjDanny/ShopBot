# ----------- main.py -----------
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from handlers import register_all_handlers

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

load_dotenv()

try:
    bot = Bot(
        token=os.getenv("TOKEN"),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    logger.info("Бот и диспетчер успешно инициализированы")
except Exception as e:
    logger.critical(f"Ошибка инициализации бота: {str(e)}")
    exit(1)

register_all_handlers(dp)
logger.info("Все обработчики зарегистрированы")

if __name__ == "__main__":
    import asyncio
    from aiogram import Dispatcher

    try:
        logger.info("Запуск бота в режиме polling...")
        asyncio.run(dp.start_polling(bot))
    except Exception as e:
        logger.critical(f"Критическая ошибка при работе бота: {str(e)}")
    finally:
        logger.info("Бот остановлен")