
from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("Fantastic")
    btn2 = KeyboardButton("Komediya")
    btn3 = KeyboardButton("Drama")
    btn4 = KeyboardButton("Triller")
    btn5 = KeyboardButton("Detective")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup
