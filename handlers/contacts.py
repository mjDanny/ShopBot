from aiogram import Router, types
from aiogram.filters import Text

router = Router()

@router.message(Text("📞 Контакты"))
async def ask_for_contacts(message: types.Message):
    await message.answer("Пожалуйста, отправьте ваши контактные данные для обратной связи.")