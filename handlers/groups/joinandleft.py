from  loader import dp
from  aiogram import bot
from  aiogram.types import Message

#
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import *
# from click import Group


@dp.message_handler(content_types=['new_chat_members'], chat_type=['group', 'supergroup'])
async def join_remover(message: Message):
    await bot.send_message(message.chat.id, f'Salom! {message.from_user.full_name} gruhimizga shush kelibsiz!')
    await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(content_types=['join_group'], chat_type=['group', 'supergroup'])
async def join_removka(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(content_types=['left_chat_member'], chat_type=['group', 'supergroup'])
async def join_removi(message: Message):
    await bot.send_message(message.chat.id, f'{message.from_user.full_name} gruhimizdan chiqib ketdi!')
    await bot.delete_message(message.chat.id, message.message_id)