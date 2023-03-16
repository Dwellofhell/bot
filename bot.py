from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile, ContentType, Message
from aiogram.utils import executor
from aiogram.utils.markdown import bold

import config
import keyboards
from config import TOKEN


bot = Bot(token=TOKEN)
dp=Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_comand(message: types.Message):
    await message.reply("Привет!\nЯ IT-cube бот, что вас интерисует?", reply_markup=keyboards.greet_kb1)

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == 'Мероприятия🎉':
        await dp.bot.send_photo(message.from_user.id, photo='AgACAgIAAxkBAAN2ZBOLAv7fhxr_bCMsdKpgr07pKy4AAi7IMRsf56BIbeVI2S2FraUBAAMCAAN5AAMvBA', caption=config.text)
    elif message.text == 'Обучение👨‍🎓':
        await dp.bot.send_message(message.from_user.id, text="Вот телеграмм с нужной тебе информацией:https: //vk.com/itcube3232")
    else:
        await dp.bot.send_message(message.from_user.id, text="Ответ мне не известен")

@dp.message_handler(commands=['help'])
async def process_help_comand(message: types.Message):
    await message.reply("Напиши, и я отвечу так же.")

@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)









if __name__ == '__main__':
    executor.start_polling(dp)
