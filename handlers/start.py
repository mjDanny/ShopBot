import os

from aiogram import Router, F, types
from keyboards.main_menu import main_menu
import logging

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.text == "↩️ Назад")
@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} нажал 'Назад' или '/start'")
    await message.answer(
        "Выберите один из вариантов ниже:",
        reply_markup=main_menu()
    )


@router.message(F.text == "/check")
async def check_permissions(message: types.Message):
    try:
        manager_chat_id = int(os.getenv("MANAGER_CHAT_ID"))
        await message.bot.send_message(
            chat_id=manager_chat_id,
            text="✅ Бот успешно подключен к этому чату!"
        )
        await message.answer("Проверка пройдена!")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {str(e)}")
