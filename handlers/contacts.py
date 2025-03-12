from aiogram import types

async def ask_for_contacts(message: types.Message):
    await message.answer("Пожалуйста, отправьте ваши контактные данные для обратной связи.")

def register_handlers(dp):
    dp.register_message_handler(ask_for_contacts, lambda message: message.text == "📞 Контакты")