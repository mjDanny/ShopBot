from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import get_services
import logging

router = Router()
logger = logging.getLogger(__name__)


# Клавиатура со списком услуг
async def services_menu_kb():
    services = await get_services()
    builder = InlineKeyboardBuilder()

    for service in services:
        builder.button(
            text=service[0],  # Название услуги
            callback_data=f"service_{service[0]}"  # Уникальный идентификатор
        )

    builder.adjust(1)  # По одной кнопке в ряд
    return builder.as_markup()


# Подробное описание услуги
async def service_details_kb(service_name: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="🛒 Заказать", callback_data=f"order_{service_name}")
    return builder.as_markup()


@router.message(F.text == "📋 Услуги")
async def show_services(message: types.Message):
    try:
        await message.answer(
            "🏷 Выберите услугу:",
            reply_markup=await services_menu_kb()
        )
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")


@router.callback_query(F.data.startswith("service_"))
async def show_service_details(callback: types.CallbackQuery):
    service_name = callback.data.split("_", 1)[1]
    services = await get_services()

    for service in services:
        if service[0] == service_name:
            response = (
                f"<b>{service[0]}</b>\n\n"
                f"{service[1]}\n\n"
                f"💵 Стоимость: {service[2]} руб.\n"
                f"🖼 Примеры: {service[3]}"
            )

            await callback.message.edit_text(
                response,
                parse_mode=ParseMode.HTML,
                reply_markup=await service_details_kb(service_name)
            )
            break