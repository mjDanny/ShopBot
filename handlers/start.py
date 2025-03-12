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