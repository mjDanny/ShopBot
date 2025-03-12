from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def services_keyboard(service_name):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("🛒 Заказать", callback_data=f"order_{service_name}")
    )