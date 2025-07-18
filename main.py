from telebot import TeleBot
from telebot.types import Message

TOKEN = "7927533842:AAEZAc1Srdh3p_O6jJUQhifQ6pMAAZuDsBA"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu alaykum")


if __name__ == '__main__':
    bot.infinity_polling()
