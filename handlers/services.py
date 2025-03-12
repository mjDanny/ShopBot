from aiogram import types
from aiogram.types import ParseMode
from keyboards.services import services_keyboard
from database import get_services

async def show_services(message: types.Message):
    services = await get_services()
    if not services:
        await message.answer("Услуги временно недоступны.")
        return

    for service in services:
        name, description, price, examples = service
        await message.answer(
            f"<b>{name}</b>\n\n"
            f"<i>{description}</i>\n\n"
            f"Цена: {price} руб.\n"
            f"Примеры: {examples}\n\n"
            "Чтобы заказать, нажмите кнопку ниже.",
            parse_mode=ParseMode.HTML,
            reply_markup=services_keyboard(name)
        )

def register_handlers(dp):
    dp.register_message_handler(show_services, lambda message: message.text == "📋 Услуги")