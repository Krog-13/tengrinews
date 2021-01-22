from inspect import Traceback
from datetime import date, time, datetime
import psycopg2 #pip3 install psycopg2-binary
from psycopg2.extras import RealDictCursor, execute_values

class SQLiter:
    def __init__(self, namedb):
        # Подключаемся к ДБ и сохроняем курсор соединения
        self.connection = psycopg2.connect(dbname=namedb, user='postgres', password='postgres', host='localhost')
        self.cursor = self.connection.cursor()

    def get_last_link(self):
        with self.connection:
            self.cursor.execute(" SELECT linck FROM post ORDER BY post_id DESC LIMIT 1")
            result = self.cursor.fetchone()
            return result

    def add_post(self, info):
        """Добавляем нового подписчика"""
        with self.connection:
            for data in info:
                self.cursor.execute("INSERT INTO post (linck, title, conntent, publish_date, publish_datetime, parse_date)"
                                           " VALUES(%s,%s,%s,%s,%s,%s)",
                                           (data[0], data[1], data[2],data[3], data[4], date.today()))
                                           #('wwewgooglwecom', 'bowwk', 'wmotwwh', date(2020,10,10), '10:10', date.today())

    def add_comment(self, info):
        """Добавляем нового подписчика"""
        for data in info:
            with self.connection:
                return self.cursor.execute("INSERT INTO coment (post_id, author, comment_date,coment, parse_date)"
                                           " VALUES(%s,%s,%s,%s,%s)",
                                           (data[0], data[1], date(2021,1,22),data[2], date.today()))

    def get_link_for_comment(self, step):
        with self.connection:
            self.cursor.execute(" SELECT post_id, linck FROM post ORDER BY post_id ASC LIMIT %s", (step,))
            result = self.cursor.fetchall()
            return result



    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()

if __name__ == '__main__':
    db =SQLiter('tengrinews')

