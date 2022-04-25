from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    Kanal = InlineKeyboardMarkup()
    Kanal.add(InlineKeyboardButton("📢 Bizning jamoa!", url="https://t.me/KhCoder"))
    Kanal.add(InlineKeyboardButton("👥Guruhga qo`shish", url="http://t.me/Join_message_removbot?startgroup=new"))
    await message.answer(f"Salom👋, {message.from_user.full_name}!\n Mening vazifam gruhdagi kirdi chiqdilarni tozalash👥 va yangi foydalanuvchi bilan salomlashish👋\n Bot to`g`ri ishlashi uchun botni gruhga ADMIN qiling🔥", reply_markup=Kanal)
