from config_data.config import horoscore_dict_rus, horoscore_dict_img
from database.horoscope_database import get_history_db
from loader import bot
import requests
from bs4 import BeautifulSoup as bs


def send_horoscope(chat_id: int) -> None:
    """
    Получает id чата. Парсим сайт для создание текста гороскопа на каждый день
    :param chat_id
    :return:
    """
    zodiac_sign = get_history_db(chat_id)
    url_template = f"https://horo.mail.ru/prediction/{zodiac_sign}/today/"
    r = requests.get(url_template)

    soup = bs(r.text, "html.parser")
    zodiac = soup.find('div', class_='p-score-day')

    text_desc = ''
    desc = zodiac.find_all('span', class_='link__text')
    val = zodiac.find_all('span', class_='p-score-day__item__value__inner')

    for i in range(len(val)):
        if val[i].text == '':
            continue
        else:
            text_desc += f'{desc[i].text} - {val[i].text}\n'

    zodiac = soup.find(class_='article__item article__item_alignment_left article__item_html').text
    text_desc += zodiac
    zodiac_sign_rus = horoscore_dict_rus[zodiac_sign]
    zodiac_path = horoscore_dict_img[zodiac_sign]
    zodiac_img = open(zodiac_path, 'rb')
    bot.send_photo(chat_id, zodiac_img, f'Твой гороскоп на сегодня {zodiac_sign_rus}: \n{text_desc}')


# Обработка команды horoscope
@bot.message_handler(commands=['horoscope'])
def get_horoscope(message: str) -> None:
    """
    ВЫВОД для команда horoscope. Используем функцию send_horoscope.
    :param message:
    :return:
    """
    send_horoscope(message.chat.id)
