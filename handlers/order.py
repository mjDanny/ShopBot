from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import get_services
import os

class OrderStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_comment = State()

async def start_order(callback: types.CallbackQuery, state: FSMContext):
    service_name = callback.data.split("_")[1]
    await state.update_data(service_name=service_name)
    await callback.message.answer("Введите ваше ФИО:")
    await OrderStates.waiting_for_name.set()

async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш контактный номер:")
    await OrderStates.waiting_for_phone.set()

async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите комментарий к заказу:")
    await OrderStates.waiting_for_comment.set()

async def process_comment(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    service_name = user_data["service_name"]
    name = user_data["name"]
    phone = user_data["phone"]
    comment = message.text

    await message.bot.send_message(
        os.getenv("MANAGER_CHAT_ID"),
        f"Новая заявка!\n\n"
        f"Услуга: {service_name}\n"
        f"Клиент: {name}\n"
        f"Контакт: {phone}\n"
        f"Комментарий: {comment}"
    )

    await message.answer("Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.")
    await state.finish()

def register_handlers(dp):
    dp.register_callback_query_handler(start_order, lambda callback: callback.data.startswith("order_"))
    dp.register_message_handler(process_name, state=OrderStates.waiting_for_name)
    dp.register_message_handler(process_phone, state=OrderStates.waiting_for_phone)
    dp.register_message_handler(process_comment, state=OrderStates.waiting_for_comment)