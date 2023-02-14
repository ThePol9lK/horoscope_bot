"""
Конфигурация бота. Объявление токена, апи-ключа и стандартных команд. Объявление базы данных
"""

import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены: отсутствует файл .env')

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

DEFAULT_COMMANDS = (
    ('help', 'Помощь'),
    ('start', 'Запустить бот'),
)

CUSTOM_COMMANDS = (
    ('settings', 'Задать знак'),
    ('horoscope', 'Посмотреть гороскоп'),
)

