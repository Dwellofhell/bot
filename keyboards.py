from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Мероприятия🎉')
button_hi1 = KeyboardButton('Обучение👨‍🎓')

greet_kb=ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi, button_hi1)

button_mr = KeyboardButton('digital-агентство')
button_mr1 = KeyboardButton('Python')
greet_mr =ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_mr1,button_mr)

button_bk=KeyboardButton('Назад к мероприятиям')
greet_bk=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button_bk)