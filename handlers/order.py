from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram import F
import os
import logging
import re

router = Router()
logger = logging.getLogger(__name__)


class OrderStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_comment = State()


PHONE_REGEX = re.compile(r"^\+\d{7,15}$")  # Регулярка для проверки телефона


@router.callback_query(F.data.startswith("order_"))
async def start_order(callback: CallbackQuery, state: FSMContext):
    try:
        service_name = callback.data.split("_", 1)[1]
        await state.update_data(service_name=service_name)
        await callback.message.answer("✏️ Введите ваше ФИО:")
        await state.set_state(OrderStates.waiting_for_name)
    except Exception as e:
        logger.error(f"Ошибка начала заказа: {str(e)}", exc_info=True)
        await callback.message.answer("⚠️ Произошла ошибка. Попробуйте позже.")
        await state.clear()


@router.message(OrderStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    if len(message.text.strip()) < 5:
        await message.answer("❌ ФИО должно содержать минимум 5 символов")
        return

    await state.update_data(name=message.text.strip())
    await message.answer("📱 Введите ваш контактный номер в формате +7XXX...:")
    await state.set_state(OrderStates.waiting_for_phone)


@router.message(OrderStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text.strip()

    if not PHONE_REGEX.match(phone):
        await message.answer("❌ Неверный формат номера. Пример: +79123456789")
        return

    await state.update_data(phone=phone)
    await message.answer("💬 Введите комментарий к заказу:")
    await state.set_state(OrderStates.waiting_for_comment)


@router.message(OrderStates.waiting_for_comment)
async def process_comment(message: types.Message, state: FSMContext):
    try:
        user_data = await state.get_data()
        comment = message.text.strip()

        text = (
            "✅ Новая заявка!\n\n"
            f"📌 Услуга: {user_data['service_name']}\n"
            f"👤 Клиент: {user_data['name']}\n"
            f"📞 Контакт: {user_data['phone']}\n"
            f"💬 Комментарий: {comment}"
        )

        manager_chat_id = os.getenv("MANAGER_CHAT_ID")
        if not manager_chat_id:
            raise ValueError("MANAGER_CHAT_ID не установлен")

        await message.bot.send_message(
            chat_id=int(manager_chat_id),
            text=text
        )
        await message.answer("🎉 Ваша заявка успешно отправлена!")

    except Exception as e:
        logger.error(f"Ошибка отправки заявки: {str(e)}", exc_info=True)
        await message.answer("⚠️ Произошла ошибка при отправке заявки")
    finally:
        await state.clear()
