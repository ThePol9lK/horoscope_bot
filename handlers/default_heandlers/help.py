"""
Базовый обработчик сообщений: выводит сообщение-помощник с существующими командами
"""


from loader import bot

@bot.message_handler(commands=['help'])
def get_help(message: str) -> None:
    """
    Вывод для команда help
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'Тут будет описание')