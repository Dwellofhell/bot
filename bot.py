from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile, ContentType, Message, MediaGroup
from aiogram.utils import executor

import config
import keyboards
from config import TOKEN


bot = Bot(token=TOKEN)
dp=Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_comand(message: types.Message):
    await message.reply("Привет!\nЯ IT-cube бот, что вас интерисует?", reply_markup=keyboards.greet_kb1)

async def send_album(message:Message):
    digital_mr=MediaGroup()
    ph1='AgACAgIAAxkBAAOxZBS6eSVgwiTg5EFKYcRnKzjQBoYAAqjHMRviq6lIlbr9kUq8goQBAAMCAAN5AAMvBA'
    ph2='AgACAgIAAxkBAAOPZBS3ljzmJFtoB_3KwmaDEioFxs8AAqXHMRviq6lIijMdnI7f2X8BAAMCAAN5AAMvB'

    digital_mr.attach_photo(photo=ph1)
    digital_mr.attach_photo(photo=ph2)
    await message.answer_media_group(media=digital_mr)

@dp.message_handler(commands=['help'])
async def process_help_comand(message: types.Message):
    await message.reply("Что бы начать напишите /start")


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == 'Мероприятия🎉':
        await dp.bot.send_photo(message.from_user.id, photo='AgACAgIAAxkBAAN2ZBOLAv7fhxr_bCMsdKpgr07pKy4AAi7IMRsf56BIbeVI2S2FraUBAAMCAAN5AAMvBA', caption='Наши мероприятия:\n1.Мы в digital-агентстве 🤩\n2.Программирование на Python', reply_markup=keyboards.greet_mr)
    elif message.text == 'Обучение👨‍🎓':
        await dp.bot.send_message(message.from_user.id, text="Вот телеграмм с нужной тебе информацией:https: //vk.com/itcube3232")
    elif message.text == 'digital-агентство':
        await dp.bot.send_photo(message.from_user.id, photo='AgACAgIAAxkBAAOPZBS3ljzmJFtoB_3KwmaDEioFxs8AAqXHMRviq6lIijMdnI7f2X8BAAMCAAN5AAMvBA', caption='Мы в digital-агентстве 🤩\n\nВоспитанники направления "Мобильная разработка" вместе с наставником Екатериной Павловной посетили digital-агентство «Веб-Центр».\n\nКомпания пригласила молодых программистов в гости на обзорную экскурсию в рамках профориентационных задач. Команда профессионалов работает с 2004 года и за это время смогла войти в ТОП-70 агентств РФ. Золотой партнер 1С-Битрикс: 1 место в рейтинге ЦФО, 2 место по России🏆', reply_markup=keyboards.greet_bk)
    elif message.text=='Python':
        await dp.bot.send_photo(message.from_user.id, photo='AgACAgIAAxkBAAP2ZBTCtQe4IGfTGrDKSXnMnZfEo58AAsfHMRviq6lIfCDOSYH9dSkBAAMCAAN5AAMvBA', caption='🧑🏼‍💻В рамках профориентационного марафона «Выбери IT» и договора о сотрудничестве с ЦОПП Брянской области, педагог-наставник направления «Программирование на Python» Алексеенко Эмилия Юрьевна провела профориентационное мероприятие «Универсальный язык Python: перспективные профессии» для обучающихся ГБПОУ «Брянский профессионально-педагогический колледж».', reply_markup=keyboards.greet_bk)
    elif message.text == 'Назад к мероприятиям':
        await dp.bot.send_photo(message.from_user.id,photo='AgACAgIAAxkBAAN2ZBOLAv7fhxr_bCMsdKpgr07pKy4AAi7IMRsf56BIbeVI2S2FraUBAAMCAAN5AAMvBA',caption='Наши мероприятия:\n1.Мы в digital-агентстве 🤩\n2.Программирование на Python',reply_markup=keyboards.greet_mr)
    else:
        await dp.bot.send_message(message.from_user.id, text="Ответ мне не известен")




@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)











if __name__ == '__main__':
    executor.start_polling(dp)
