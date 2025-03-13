from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import os
import logging

router = Router()
logger = logging.getLogger(__name__)


class ContactStates(StatesGroup):
    waiting_for_contact = State()


async def validate_chat_id(bot, chat_id: int) -> bool:
    """Проверяет, может ли бот отправлять сообщения в чат"""
    try:
        await bot.get_chat(chat_id)
        return True
    except Exception as e:
        logger.error(f"Chat validation failed: {str(e)}")
        return False


@router.message(F.text == "📞 Оставить контакты")
async def request_contact(message: types.Message, state: FSMContext):
    await state.set_state(ContactStates.waiting_for_contact)
    await message.answer("📝 Введите ваш контакт для связи:")


@router.message(ContactStates.waiting_for_contact)
async def process_contact(message: types.Message, state: FSMContext):
    try:
        # Получаем и валидируем chat_id
        manager_chat_id = int(os.getenv("MANAGER_CHAT_ID"))
        logger.info(f"Attempting to send to chat: {manager_chat_id}")

        if not await validate_chat_id(message.bot, manager_chat_id):
            await message.answer("❌ Ошибка: бот не имеет доступа к целевому чату")
            return

        # Отправка сообщения
        await message.bot.send_message(
            chat_id=manager_chat_id,
            text=f"📩 Новый контакт от @{message.from_user.username}:\n{message.text}",
        )
        logger.info(f"Message sent to {manager_chat_id} successfully")

        await message.answer("✅ Данные успешно отправлены!")
        await state.clear()

    except ValueError:
        logger.error("Invalid MANAGER_CHAT_ID format")
        await message.answer("❌ Ошибка конфигурации бота")
    except Exception as e:
        logger.error(f"Critical error: {str(e)}", exc_info=True)
        await message.answer("⚠️ Произошла критическая ошибка")
    finally:
        await state.clear()
