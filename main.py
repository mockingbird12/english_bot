import telebot
from service import main_markup
from telebot import apihelper, types
from database.insert import update_status
from database.insert import get_user_status
from database.insert import insert_word
from database.insert import insert_translate
import config


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['add_words'])
def add_words(message):
    bot.send_message(message.chat.id, "Add new words")


@bot.message_handler(commands=['start'])
def admin_login(message):
    bot.send_message(message.chat.id, "Let's check your words")


@bot.message_handler(content_types=['text'], func=lambda message:get_user_status(message.chat.id) == 'enter_translate')
def add_translate(message):
    translate = message.text
    insert_translate(translate)
    bot.send_message(message.chat.id, 'Word and translate successfully added')
    update_status(message.chat.id, None)

@bot.message_handler(content_types=['text'],func=lambda message:get_user_status(message.chat.id) == 'enter_word')
def add_word(message):
    word = message.text
    insert_word(word)
    bot.send_message(message.chat.id, 'Input translate')
    update_status(message.chat.id, 'enter_translate')


@bot.callback_query_handler(func=lambda callback_query: callback_query.data)
def users_choice(callback_query: types.CallbackQuery):
    code = callback_query.data
    # bot.answer_callback_query(callback_query.from_user.id, 'Add new word')
    update_status(callback_query.from_user.id, 'enter_word')
    bot.send_message(callback_query.from_user.id, 'Input new word')
    print (get_user_status(callback_query.from_user.id))



@bot.message_handler(content_types=['text'], func=lambda message: get_user_status(message.chat.id) == None)
def send_welcome(message):
    bot.send_message(message.chat.id, "English speeking bot")
    bot.send_message(message.chat.id, config.START_MSG, reply_markup=main_markup())


if __name__ == '__main__':
    print('Starting bot')
    while True:
        try:
            temp_host = '192.168.100.30:9100'
            apihelper.proxy = {'https': 'socks5://' + temp_host}
            bot.polling(none_stop=True)
        except Exception:
            pass