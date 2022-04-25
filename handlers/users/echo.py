from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    text = 'Mavjud bo`lmagan buyruq ✖'
    await message.answer(text)
