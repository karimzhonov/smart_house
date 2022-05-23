from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart
from config import TELEGRAM_BOT_TOKEN
from core.dialog import get_answer

__all__ = ['dp']

dp = Dispatcher(Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML))


async def commond_start(msg: types.Message):
    text = 'This is bot for smart house'
    await msg.answer(text)


async def get_sentence_from_user(msg: types.Message):
    answer = get_answer(msg.text)
    await msg.answer(answer)


dp.register_message_handler(commond_start, CommandStart())
dp.register_message_handler(get_sentence_from_user)
