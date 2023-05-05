from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Мероприятия🎉')
button_hi1 = KeyboardButton('Обучение👨‍🎓')


greet_kb1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi, button_hi1)

button_mr = KeyboardButton('digital-агентство')
button_mr1 = KeyboardButton('Python')
button_bk1 = KeyboardButton('Вернуться на главную')
greet_mr =ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,row_width=2).add(button_mr1,button_mr).insert(button_bk1)

button_bk=KeyboardButton('Назад к мероприятиям')
greet_bk=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button_bk)


button_py=KeyboardButton('Курсы Python')
button_js = KeyboardButton('Курсы JavaScript')
greet_study = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,row_width=2).add(button_js,button_py).insert(button_bk1)

il_button_join = InlineKeyboardButton('Записаться', callback_data='button1')
inline1=InlineKeyboardMarkup().add(il_button_join)

back_to_study = KeyboardButton('Назад к курсам')
greet_study_bk = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(back_to_study)