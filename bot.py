from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import keyboards
from config import TOKEN


bot = Bot(token=TOKEN)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_comand(message: types.Message):
    await message.reply("Привет!\nЯ IT-cube бот, что вас интерисует?", reply_markup=keyboards.greet_kb)


@dp.message_handler(commands=['help'])
async def process_help_comand(message: types.Message):
    await message.reply("Напиши, и я отвечу так же.")

@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=keyboards.greet_kb1)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)





if __name__ == '__main__':
    executor.start_polling(dp)
