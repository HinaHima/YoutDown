import state
from loader import dp, bot
from aiogram import types
from state import Url
from video_option import search_youtube
import markup
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['start', 'help'])
async def commands(message: types.Message):
    if message.text == '/start':
        await bot.send_message(message.from_user.id,'Hello, this bot can help you download videos from Youtube if possible. Type "/help" for more info.')
    if message.text == '/help':
        await bot.send_message(message.from_user.id, 'First of all you need to copy the URL of the video you want to download. '
                                                     'Then press the button that below and paste the URL. '
                                                     'After this choose the resolution needed and wait for the bot to download the video.',
                               reply_markup=markup.start)

@dp.callback_query_handler(text='btn_search')
async def search(message: types.Message):
    await bot.send_message(message.from_user.id, "Paste the URl:")

    await Url.url_info.set()

@dp.message_handler(state=state.Url.url_info)
async def load_options(message: types.Message, state: FSMContext):
    url = message.text
    await state.update_data(
        {"url": url}
    )

    video = message.text
    videos = search_youtube(video)

    choices = {}

    resolutions = ['720p', '1080p', '1440p']

    try:
        for each_resolution in resolutions:
            choice = videos.streams.filter(res={each_resolution})
            choices[each_resolution] = choice[0]
    except IndexError:
        Error_1 = f"Havn't found any video in such resolution: {each_resolution}. Please try another"
        await bot.send_message(message.from_user.id, Error_1)


    for i in choices.keys():
        await bot.send_message(message.from_user.id, i)

    await bot.send_message(message.from_user.id, "There are the resolutions found, choose one of them.",
                           reply_markup=markup.resolutions)

@dp.callback_query_handler(text='btn_720p')
async def search(message: types.Message, state: FSMContext):
    data = await state.get_data()
    url = data.get("url")
    videos = search_youtube(url)
    video = videos.streams.filter(res='720p')
    try:
        video_needed = video[0]
        video_needed.download()
    except IndexError:
        Error_1 = "Havn't found any video in such resolution. Please try another"
        await bot.send_message(message.from_user.id, Error_1)
    await bot.send_message(message.from_user.id, "Downloading the video")
    await state.reset_state()

