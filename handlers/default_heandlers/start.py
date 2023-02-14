from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['start'])
def get_start(message: Message) -> None:
    """
    ВЫВОД для команда start
    :param message:
    :return:
    """
    bot.send_message(chat_id=message.chat.id, text='Добро пожаловать в бота для гороскопа',
                     parse_mode='html')
