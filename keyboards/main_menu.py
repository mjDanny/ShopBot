from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    """Создание reply-клавиатуры главного меню"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Услуги")],  # Кнопка просмотра услуг
            [
                KeyboardButton(text="📞 Оставить контакты"),  # Кнопка контактов
                KeyboardButton(text="↩️ Назад")     # Кнопка возврата
            ]
        ],
        resize_keyboard=True,         # Автоматическое изменение размера кнопок
        input_field_placeholder="Выберите действие..."  # Подсказка в поле ввода
    )