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