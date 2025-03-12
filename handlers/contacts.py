from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import os
import logging

router = Router()
logger = logging.getLogger(__name__)

class ContactStates(StatesGroup):
    waiting_for_contact = State()

@router.message(F.text == "📞 Оставить контакты")
async def request_contact(message: types.Message, state: FSMContext):
    await message.answer("📱 Пожалуйста, напишите ваш контактный номер телефона:")
    await state.set_state(ContactStates.waiting_for_contact)

@router.message(ContactStates.waiting_for_contact)
async def process_contact(message: types.Message, state: FSMContext):
    try:
        manager_chat_id = os.getenv("MANAGER_CHAT_ID")
        if not manager_chat_id:
            await message.answer("⚠️ Ошибка конфигурации бота")
            return

        await message.bot.send_message(
            chat_id=int(manager_chat_id),  # Преобразуем в число
            text=f"📬 Новый контакт:\n{message.text}"
        )
        await message.answer("✅ Данные отправлены!")
        await state.clear()

    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        await message.answer("⚠️ Ошибка отправки")
        await state.clear()
