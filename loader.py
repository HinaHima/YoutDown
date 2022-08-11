# loading modules and frameworks needed
import logging
from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube

# loading the token for the bot

from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)