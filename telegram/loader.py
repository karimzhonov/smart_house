from aiogram import types as _types
from aiogram import Bot as _Bot
from aiogram import Dispatcher as _Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage as _MemoryStorage
from config import TELEGRAM_BOT_TOKEN

dp = _Dispatcher(_Bot(TELEGRAM_BOT_TOKEN, parse_mode=_types.ParseMode.HTML), storage=_MemoryStorage())
