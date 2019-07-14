import telebot
from service import gen_markup
from telebot import apihelper
import config


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['add_words'])
def add_words(message):
    bot.send_message(message.chat.id, "Add new words")

@bot.message_handler(commands=['start'])
def admin_login(message):
    bot.send_message(message.chat.id, "Let's check your words")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.send_message(message.chat.id, "English speeking bot")
    bot.send_message(message.chat.id, config.START_MSG)


apihelper.proxy = {'https': 'socks5://127.0.0.1:9050'}
bot.polling(none_stop=True)