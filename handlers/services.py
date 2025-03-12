from aiogram import Router, types
from aiogram import F
from database import get_services
from keyboards.services import services_keyboard

router = Router()

@router.message(F.Text("📋 Услуги"))
async def show_services(message: types.Message):
    try:
        services = await get_services()
        if not services:
            await message.answer("😞 В данный момент услуги недоступны")
            return

        for service in services:
            name, desc, price, examples = service
            response = (
                f"<b>{name}</b>\n\n"
                f"<i>{desc}</i>\n\n"
                f"💵 Стоимость: {price} руб.\n"
                f"🖼 Примеры: {examples}"
            )
            await message.answer(
                text=response,
                reply_markup=services_keyboard(name)
            )
    except Exception as e:
        await message.answer("⚠️ Не удалось загрузить информацию об услугах")