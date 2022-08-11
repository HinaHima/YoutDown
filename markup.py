from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn_search = InlineKeyboardButton ('Paste the URL of the video you want to download', callback_data='btn_search')
btn_reso_720 = InlineKeyboardButton ('720p', callback_data='btn_reso_720')
btn_reso_1080 = InlineKeyboardButton ('720p', callback_data='btn_reso_1080')

start = InlineKeyboardMarkup().add(btn_search)
resolution = InlineKeyboardMarkup().add(btn_reso_720).add(btn_reso_1080)