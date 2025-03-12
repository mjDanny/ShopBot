from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def services_keyboard(service_name: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 Заказать", callback_data=f"order_{service_name}")]
        ]
    )