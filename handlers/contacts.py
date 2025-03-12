from aiogram import Router, types
from aiogram import F

router = Router()


@router.message(F.text == "📞 Контакты")
async def ask_for_contacts(message: types.Message):
    await message.answer("Пожалуйста, отправьте ваши контактные данные для обратной связи.")
