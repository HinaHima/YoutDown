import loader
import handlers
from aiogram import executor
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    executor.start_polling(loader.dp, skip_updates = True)
