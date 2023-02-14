from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def voice_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
        *(
            InlineKeyboardButton(text="Cледующее голосовок ➡", callback_data='photo_next'),
        )
    )