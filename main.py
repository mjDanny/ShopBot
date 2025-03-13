import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from handlers import register_all_handlers  # Импорт функции регистрации обработчиков

# Загрузка переменных окружения из файла .env
load_dotenv()

# Инициализация бота с токеном из переменных окружения
bot = Bot(
    token=os.getenv("TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Установка HTML-разметки по умолчанию
)

# Инициализация хранилища состояний в памяти
storage = MemoryStorage()

# Создание диспетчера с указанным хранилищем
dp = Dispatcher(storage=storage)

# Регистрация всех обработчиков из папки handlers
register_all_handlers(dp)

# Запуск бота в режиме polling (опрос серверов Telegram)
if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))