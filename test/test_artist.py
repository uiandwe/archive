#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
import pytest
import pymysql

from controllers.DbController import DbController
from controllers import artistController
xfail = pytest.mark.xfail
dc = DbController()


def test_artist_count():
    filed = "name"
    page = 0
    return_json = artistController.get_artists(dc, filed, page)

    assert len(return_json['data']) == 50

    assert return_json['data'][0].get('name') == "빈센트 반 고흐"



