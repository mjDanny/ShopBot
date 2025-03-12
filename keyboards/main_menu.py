from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Услуги")],
            [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="↩️ Назад")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )