from loader import bot
import requests
from bs4 import BeautifulSoup as bs


def send_horoscope(chat_id: int) -> None:
    """
    Получает id чата. Парсим сайт для создание текста гороскопа на каждый день
    :param chat_id: int
    :return: chat_id, text_desc -> str
    """
    url_template = "https://horo.mail.ru/prediction/scorpio/today/"
    r = requests.get(url_template)

    soup = bs(r.text, "html.parser")
    skoprio = soup.find('div', class_='p-score-day')

    text_desc = ''
    desc = skoprio.find_all('span', class_='link__text')
    val = skoprio.find_all('span', class_='p-score-day__item__value__inner')

    for i in range(len(val)):
        if val[i].text == '':
            continue
        else:
            text_desc += f'{desc[i].text} - {val[i].text}\n'

    skoprio = soup.find(class_='article__item article__item_alignment_left article__item_html').text
    text_desc += skoprio

    bot.send_message(chat_id, f'Твой гороскоп на сегодня: \n{text_desc}')


# Обработка команды horoscope
@bot.message_handler(commands=['horoscope'])
def get_horoscope(message: str) -> None:
    """
    ВЫВОД для команда horoscope. Используем функцию send_horoscope.
    :param message:
    :return:
    """
    send_horoscope(message.chat.id)
