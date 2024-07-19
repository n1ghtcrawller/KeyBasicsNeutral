
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = "7465102165:AAHOO7PKWEBtZFMLon2Glar_NM2jirbUUm0"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть сайт', web_app=WebAppInfo(url='')))
    await message.answer("Hello.", reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)