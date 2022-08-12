from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn_search = InlineKeyboardButton ('Paste the URL of the video you want to download', callback_data='btn_search')
btn_720p = InlineKeyboardButton ('720p resolution', callback_data='btn_720p')
btn_1080p = InlineKeyboardButton ('1080p resolution', callback_data='btn_1080p')
btn_1440p = InlineKeyboardButton ('1440p resolution', callback_data='btn_1440p')

start = InlineKeyboardMarkup().add(btn_search)
resolutions = InlineKeyboardMarkup().add(btn_720p).add(btn_1080p).add(btn_1440p)