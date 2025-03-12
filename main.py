import os
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers import start, services, order, contacts

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Регистрация обработчиков
start.register_handlers(dp)
services.register_handlers(dp)
order.register_handlers(dp)
contacts.register_handlers(dp)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)