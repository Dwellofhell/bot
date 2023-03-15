from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def process_start_comand(message: types.Message):
    await message.reply("Привет!\nЯ IT-cube бот, у меня ты можешь узнать ответы на интересующие тебя вопросы.")


@dp.message_handler(commands=['help'])
async def process_help_comand(message: types.Message):
    await message.reply("Напиши, и я отвечу так же.")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
