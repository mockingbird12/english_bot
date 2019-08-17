from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 7
    markup.add(InlineKeyboardButton("1", callback_data=1),
               InlineKeyboardButton("2", callback_data=2),
               InlineKeyboardButton("3", callback_data=3),
               InlineKeyboardButton("4", callback_data=4),
               InlineKeyboardButton("5", callback_data=5),
               InlineKeyboardButton("6", callback_data=6),
               InlineKeyboardButton("7", callback_data=7),
               InlineKeyboardButton("8", callback_data=8),
               )
    return markup

def main_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Add word', callback_data='add_word'),
            #   InlineKeyboardButton("Start Test", callback_data='start_test')
               )
    return markup

def check_user():
    pass

def add_word(word_data):
    # word_data - dictionary {'word':'some_word', 'translate':'word_translate'}
    pass