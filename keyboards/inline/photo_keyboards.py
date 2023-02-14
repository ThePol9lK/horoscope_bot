from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def photo_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
        *(
            InlineKeyboardButton(text="Cледующее фото ➡", callback_data='photo_next'),
        )
    )