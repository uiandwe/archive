__author__ = 'hyeonsj'
import pymysql
from config import config


class DbController:

    conn = None
    cur = None

    def __init__(self):
        try:
            conn = pymysql.connect(host=config.host, user=config.user, passwd=config.passwd, db=config.db,
                                   charset=config.charset)
            self.conn = conn
            self.cur = conn.cursor()
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            return code, message

    def get_cursor(self):
        return self.cur

    def close_db(self):
        try:
            self.cur.close()
            self.conn.close()
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            return code, message

    def execute_sql(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()

            return self.cur

        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            return code, message
