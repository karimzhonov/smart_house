from aiogram import types
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TELEGRAM_BOT_TOKEN

__all__ = ['dp']

dp = Dispatcher(Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML), storage=MemoryStorage())
