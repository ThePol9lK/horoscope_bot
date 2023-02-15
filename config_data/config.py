"""
Конфигурация бота. Объявление токена, апи-ключа и стандартных команд. Объявление базы данных
"""

import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены: отсутствует файл .env')

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

horoscore_dict_rus = dict(aries='Овен', taurus='Телец', gemini='Близнецы', cancer='Рак', leo='Лев', libra='Весы',
                          virgo='Дева', scorpio='Скорпион', sagittarius='Стрелец', capricorn='Козерог',
                          aquarius='Водолей', pisces='Рыбы')
horoscore_dict_img = dict(aries='crs/aries.png', taurus='Телец', gemini='Близнецы', cancer='Рак', leo='Лев', libra='Весы',
                          virgo='Дева', scorpio='crs/scopr.png', sagittarius='Стрелец', capricorn='Козерог',
                          aquarius='Водолей', pisces='Рыбы')

DEFAULT_COMMANDS = (
    ('help', 'Помощь'),
    ('start', 'Запустить бот'),
)

CUSTOM_COMMANDS = (
    ('settings', 'Задать знак'),
    ('horoscope', 'Посмотреть гороскоп'),
)
