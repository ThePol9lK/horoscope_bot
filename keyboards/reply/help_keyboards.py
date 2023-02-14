from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def help_markup() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
        *(
            KeyboardButton('хочу фото 🖼'),
            KeyboardButton('хочу голосовое 🎶'),
            KeyboardButton('хочу открыть печеньку 🥠'),
            KeyboardButton('хочу гороскоп ♏'),
            KeyboardButton('хочу погоду ☀')
        )
    )
