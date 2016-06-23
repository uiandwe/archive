__author__ = 'hyeonsj'
import pytest
import pymysql

from controllers.DbController import DbController
xfail = pytest.mark.xfail
dc = DbController()


def test_connect():
    assert type(dc.get_cursor()) == pymysql.cursors.Cursor


def test_find():
    sql = "select count(*) from artists;"
    cur = dc.find(sql)
    for temp_count in cur:
        assert temp_count[0] == 50

@xfail
def test_fail_insert():
    sql = "Insert into images (image_url, title, year, artist_id, description) " \
          "Values " \
          "('https://en.wikipedia.org/wiki/The_Last_Supper_(Leonardo_da_Vinci)#" \
          "/media/File:%C3%9Altima_Cena_-_Da_Vinci_5.jpg', 'The Last Supper', 1495, 151, '캔버스에 유채');"
    cur = dc.insert(sql)
    for temp_pk in cur:
        assert temp_pk[0] == 69

@xfail
def test_fail_find():
    sql = "select count(*) from images;"
    cur = dc.find(sql)
    for temp_count in cur:
        assert temp_count[0] == 65


def test_update():
    sql = "update images set title='The Last Supper2' where title = 'The Last Supper'"
    dc.update(sql)
    sql = "select count(*) from images where title='The Last Supper2';"
    cur = dc.find(sql)
    for temp_count in cur:
        assert temp_count[0] == 1


def test_delete():
    sql = "delete from images where title = 'The Last Supper2'"
    dc.delete(sql)

    sql = "select count(*) from images;"
    cur = dc.find(sql)
    for temp_count in cur:
        assert temp_count[0] == 65


@xfail
def test_close():
    assert type(dc.close_db()) == pymysql.cursors.Cursor


