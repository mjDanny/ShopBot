import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from handlers import register_all_handlers

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация всех обработчиков
register_all_handlers(dp)

# Запуск бота
if __name__ == "__main__":
    import asyncio
    from aiogram import Dispatcher
    asyncio.run(dp.start_polling(bot))