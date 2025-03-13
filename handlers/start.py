from aiogram import Router, F, types
from keyboards.main_menu import main_menu  # Импорт клавиатуры главного меню

router = Router()

@router.message(F.text == "↩️ Назад")
@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    """Обработчик команд /start и кнопки 'Назад'"""
    await message.answer(
        "Главное меню:",
        reply_markup=main_menu()  # Показ главного меню
    )