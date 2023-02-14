from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def text_markup() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
        *(
            KeyboardButton('ПОМОГИТЕ🐀'),
        )
    )
