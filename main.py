import telebot
from service import main_markup
from telebot import apihelper, types
import config


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['add_words'])
def add_words(message):
    bot.send_message(message.chat.id, "Add new words")


@bot.message_handler(commands=['start'])
def admin_login(message):
    bot.send_message(message.chat.id, "Let's check your words")

#
# @bot.callback_query_handler(func=lambda c: c.data and c.data == 'add_word')
# async def start_test(callback_querry: types.CallbackQuery):
#     code = callback_querry.data
#     await bot.answer_callback_query(callback_querry.from_user.id, 'Start testing')


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'add_word')
def add_word(callback_query: types.CallbackQuery):
    code = callback_query.data
    bot.answer_callback_query(callback_query.from_user.id, 'Add new word')
    # await bot.send_message(callback_query.from_user.id, 'Add new word')


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.send_message(message.chat.id, "English speeking bot")
    bot.send_message(message.chat.id, config.START_MSG, reply_markup=main_markup())


if __name__ == '__main__':
    temp_host = '192.168.100.30:9100'
    apihelper.proxy = {'https': 'socks5://' + temp_host}
    bot.polling(none_stop=True)