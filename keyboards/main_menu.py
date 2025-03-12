from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Услуги")],
            [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="🛒 Заказать")]
        ],
        resize_keyboard=True
    )
