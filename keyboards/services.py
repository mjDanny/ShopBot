from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def services_keyboard(service_name: str):
    """Создание инлайн-клавиатуры для конкретной услуги"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                # Кнопка заказа с callback_data в формате order_НАЗВАНИЕ_УСЛУГИ
                InlineKeyboardButton(
                    text="🛒 Заказать", callback_data=f"order_{service_name}"
                )
            ]
        ]
    )


async def services_menu_kb():
    """Клавиатура со списком всех услуг"""
    from database import (
        get_services,
    )  # Локальный импорт для избежания циклических зависимостей

    services = await get_services()
    builder = InlineKeyboardBuilder()

    # Добавление кнопок для каждой услуги
    for service in services:
        builder.button(
            text=service[0],  # Название услуги
            callback_data=f"service_{service[0]}",  # Уникальный идентификатор
        )

    # Расположение кнопок по одной в ряд
    builder.adjust(1)
    return builder.as_markup()
