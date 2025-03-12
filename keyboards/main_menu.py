from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("📋 Услуги")],
            [KeyboardButton("📞 Контакты"), KeyboardButton("🛒 Заказать")]
        ],
        resize_keyboard=True
    )