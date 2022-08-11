from aiogram.dispatcher.filters.state import StatesGroup, State

class Url(StatesGroup):
    url_info = State()
    res_choice = State()