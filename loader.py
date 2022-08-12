# loading modules and frameworks needed
import logging
from aiogram import Bot, Dispatcher, types
from pytube import YouTube
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# loading the token for the bot

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())