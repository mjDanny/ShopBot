from aiogram import Router, F, types
from keyboards.main_menu import main_menu  # Импорт клавиатуры главного меню

router = Router()


@router.message(F.text == "↩️ Назад")
@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    """Обработчик команды /start и кнопки 'Назад'"""
    welcome_text = (
        "👋 Добро пожаловать в мини-магазин рекламного агентства!\n\n"
        "Здесь вы можете:\n"
        "📋 Просмотреть доступные услуги\n"
        "📞 Оставить контактные данные\n"
        "🛒 Оформить заказ\n\n"
        "Выберите действие:"
    )

    await message.answer(
        welcome_text,
        reply_markup=main_menu()  # Показ главного меню
    )