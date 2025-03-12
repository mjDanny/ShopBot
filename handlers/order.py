from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
import os

router = Router()


class OrderStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_comment = State()


@router.callback_query(Text(startswith="order_"))
async def start_order(callback: CallbackQuery, state: FSMContext):
    try:
        service_name = callback.data.split("_", 1)[1]
        await state.update_data(service_name=service_name)
        await callback.message.answer("✏️ Введите ваше ФИО:")
        await state.set_state(OrderStates.waiting_for_name)
    except Exception as e:
        await callback.message.answer("⚠️ Произошла ошибка. Попробуйте позже.")
        await state.clear()


@router.message(OrderStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer("❌ ФИО должно содержать минимум 5 символов")
        return

    await state.update_data(name=message.text)
    await message.answer("📱 Введите ваш контактный номер в формате +7XXX...:")
    await state.set_state(OrderStates.waiting_for_phone)


@router.message(OrderStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    if not message.text.startswith("+"):
        await message.answer("❌ Номер должен начинаться с '+'")
        return

    await state.update_data(phone=message.text)
    await message.answer("💬 Введите комментарий к заказу:")
    await state.set_state(OrderStates.waiting_for_comment)


@router.message(OrderStates.waiting_for_comment)
async def process_comment(message: types.Message, state: FSMContext):
    try:
        user_data = await state.get_data()
        text = (
            "✅ Новая заявка!\n\n"
            f"📌 Услуга: {user_data['service_name']}\n"
            f"👤 Клиент: {user_data['name']}\n"
            f"📞 Контакт: {user_data['phone']}\n"
            f"💬 Комментарий: {message.text}"
        )

        await message.bot.send_message(
            chat_id=os.getenv("MANAGER_CHAT_ID"),
            text=text
        )
        await message.answer("🎉 Ваша заявка успешно отправлена!")
    except Exception as e:
        await message.answer("⚠️ Произошла ошибка при отправке заявки")
    finally:
        await state.clear()