from aiogram import types
from keyboards.main_menu import main_menu

async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать! Выберите действие:",
        reply_markup=main_menu()
    )

def register_handlers(dp):
    dp.register_message_handler(cmd_start, commands=["start"])