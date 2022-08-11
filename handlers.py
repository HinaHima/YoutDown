import state
from loader import dp, bot
from aiogram import types
from state import Url
from video_option import search_youtube
from markup import start, resolution
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['start', 'help'])
async def commands(message: types.Message):
    if message == 'start':
        await bot.send_message(message.from_user.id,'Hello, this bot can help you download videos from Youtube if possible. Type "/help" for more info.')
    if message == 'help':
        await bot.send_message(message.from_user.id, 'First of all you need to copy the URL of the video you want to download. '
                                                     'Then press the button that below and paste the URL. '
                                                     'After this choose the resolution needed and wait for the bot to download the video.',
                               reply_markup=start)

@dp.message_handler(text='btn_search')
async def search(message: types.Message):
    await bot.send_message(message.from_user.id, "Paste the URl:")

    await Url.url_info.set()

@dp.message_handler(state=state.Url.url_info)
async def do_search(message: types.Message, state: FSMContext):
    video_url = message.text

    await state.update_data(
        {"video_url" : video_url}
    )

    await bot.send_message(message.from_user.id, reply_markup=resolution)

    await Url.res_choice.set()

@dp.message_handler(text='btn_reso_720')
async def load_720(message: types.Message, state: FSMContext):
    data = await state.get_data()
    resolution_choice_720 = message.text
    video_url = data.get("video_url")
    video = search_youtube(video_url)
    videos = video.streams.filter(res="720p")

    quantity = 0
    choices = {}

    for each_video in videos:
        quantity += 1
        number = quantity
        choices[number] = videos.itag_index
