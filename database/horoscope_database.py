import sqlite3


def create_table():
    """Функция создаёт таблицe в базу данных если её не существует."""
    with sqlite3.connect('database/horoscope.db') as con:
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS horoscope_telebot (
            user_id INTEGER,
            zodiac_sign TEXT)
        """
        )


def update_history_db(user_id: int, zodiac_sign: str):
    """ Сохранение данных о запросе в базу данных.
        :params user_id: id пользователя
                username: имя пользователя
                command: команду которую ввел пользователь
                command_date: дата когда была введена команда
                photo: фото отеля
                hotels: информация об отелях
    """
    with sqlite3.connect('database/horoscope.db') as con:
        cur = con.cursor()
        user = con.execute('SELECT * FROM horoscope_telebot WHERE user_id=%d' % user_id).fetchall()
        if not user:
            cur.execute("""INSERT INTO 'horoscope_telebot' (user_id, zodiac_sign) VALUES (?, ?)""",
                        (user_id, zodiac_sign,))
        else:
            cur.execute("""UPDATE horoscope_telebot SET zodiac_sign == (?) WHERE user_id = (?)""",
                        (zodiac_sign, user_id,))


def get_history_db(chat_id: int) -> list:
    """"""

    with sqlite3.connect('database/horoscope.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT zodiac_sign from horoscope_telebot WHERE user_id == (?)
            """, (chat_id,)
        )
        result = cur.fetchone()
        return result[0]
