#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
import pytest

from controllers.DbController import db_session
from models.models import Artist
from controllers import artistController
xfail = pytest.mark.xfail


def test_artists_get():
    a = Artist()
    artist_query = db_session.query(Artist)
    artist_list = a.to_dict(artist_query)

    assert artist_list[0]['id'] == 102


# def test_delete_all_artists():
#
#     db_session.query(Artist).delete()
#     db_session.commit()
#     return_value = db_session.query(Artist).count()
#
#     assert return_value == 0

def test_artists_post():

    name = ""
    birth_year = 1000
    death_year = 1100
    country = "korea"
    genre = "표현주의"

    return_json = artistController.post_artists(name, birth_year, death_year, country, genre)
    assert return_json['code'] == "NotInput"


    name = "현승재"
    birth_year = 1000
    death_year = 1100
    country = "12345678901234567890123456789012345678901234567890"
    genre = "표현주의"
    return_json = artistController.post_artists(name, birth_year, death_year, country, genre)
    assert return_json['code'] == "OutOfRangeInput"

    name = "현승재"
    birth_year = 1985
    death_year = 1000
    country = "korea"
    genre = "표현주의"

    return_json = artistController.post_artists(name, birth_year, death_year, country, genre)
    assert return_json['code'] == "WrongInput"


def test_artist_get():

    return_json = artistController.get_artist(None, 105)

    assert return_json['data']['name'] == "존 밀레이"


def test_artist_update():

    name = "현승재2"
    birth_year = 1000
    death_year = 1100
    country = "korea2"
    genre = "표현주의2"
    return_json = artistController.put_artist(154, name, birth_year, death_year, country, genre)

    assert return_json['code'] == 200


def test_artist_delete():

    return_json = artistController.delete_artists(155)
    assert return_json['code'] == 200

