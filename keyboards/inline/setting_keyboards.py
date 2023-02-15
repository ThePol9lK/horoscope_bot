from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def settings_markup() -> InlineKeyboardMarkup:
    """ Клавиатура для выбора знака зодиака """
    keyboard = InlineKeyboardMarkup()
    button_aries = InlineKeyboardButton(text='Овен', callback_data='aries')
    button_taurus = InlineKeyboardButton(text='Телец', callback_data='taurus')
    button_twins = InlineKeyboardButton(text='Близнецы', callback_data='gemini')
    button_cancer = InlineKeyboardButton(text='Рак', callback_data='cancer')
    button_lion = InlineKeyboardButton(text='Лев', callback_data='leo')
    button_virgo = InlineKeyboardButton(text='Дева', callback_data='virgo')
    button_scales = InlineKeyboardButton(text='Весы', callback_data='libra')
    button_scorpion = InlineKeyboardButton(text='Скорпион', callback_data='scorpio')
    button_sagittarius = InlineKeyboardButton(text='Стрелец', callback_data='sagittarius')
    button_capricorn = InlineKeyboardButton(text='Козерог', callback_data='capricorn')
    button_aquarius = InlineKeyboardButton(text='Водолей', callback_data='aquarius')
    button_fish = InlineKeyboardButton(text='Рыбы', callback_data='pisces')
    keyboard.add(button_aries, button_taurus, button_twins, button_cancer, button_lion, button_virgo, button_scales,
                 button_scorpion, button_sagittarius, button_capricorn, button_aquarius, button_fish)
    return keyboard
