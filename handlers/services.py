from aiogram import Router, types
from aiogram import F
from database import get_services
from keyboards.services import services_keyboard

import logging

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.text == "📋 Услуги")
async def show_services(message: types.Message):
    logger.info("Обработчик услуг вызван!")
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил услуги")
        services = await get_services()

        if not services:
            logger.warning("Нет доступных услуг в базе данных")
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
            logger.debug(f"Отправлена услуга: {name}")

    except Exception as e:
        logger.error(f"Ошибка показа услуг: {str(e)}", exc_info=True)
        await message.answer("⚠️ Произошла ошибка при загрузке услуг")
