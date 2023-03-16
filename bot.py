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
    await message.reply("Привет!\nЯ IT-cube бот, что вас интерисует?", reply_markup=keyboards.greet_kb1)


@dp.message_handler(commands=['help'])
async def process_help_comand(message: types.Message):
    await message.reply("Напиши, и я отвечу так же.")


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == 'Мероприятия🎉':
        await bot.send_message(message.from_user.id,text="Вот группа вк с нужной тебе информацией:https: //vk.com/itcube3232")
    elif message.text == 'Обучение👨‍🎓':
        await bot.send_message(message.from_user.id, text="Вот телеграмм с нужной тебе информацией:https: //vk.com/itcube3232")
    else:
        await bot.send_message(message.from_user.id, text="Ответ мне не известен")






if __name__ == '__main__':
    executor.start_polling(dp)
