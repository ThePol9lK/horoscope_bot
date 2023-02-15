from telebot.types import CallbackQuery

from database.horoscope_database import update_history_db
from loader import bot
from keyboards.inline.setting_keyboards import settings_markup


@bot.message_handler(commands=['settings'])
def get_horoscope(message: str) -> None:
    """
        Выбор пользователем знака зодиака
        :param message:
        :return:
        """
    bot.send_message(message.chat.id, 'Выбери знак зодиака', reply_markup=settings_markup())


@bot.callback_query_handler(func=lambda call: True)
def insert_horoscope(call: CallbackQuery):
    bot.edit_message_text('Я записал значение напиши команду /horoscope', call.from_user.id, call.message.id)
    bot.delete_message(call.from_user.id, call.message.id-1)
    update_history_db(user_id=call.from_user.id, zodiac_sign=call.data)
    print(call.from_user.id, call.data)
