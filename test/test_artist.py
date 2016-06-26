#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
import pytest

from controllers.DbController import DbController
from controllers import artistController
from models import ArtistModel
xfail = pytest.mark.xfail
dc = DbController()


def test_artists_get():
    filed = "name"
    page = 0
    artist_Model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_Model.get(filed)

    # assert len(artist_list) == 50

    assert artist_list[0].name == "빈센트 반 고흐"


# def test_delete_all_artists():
#     artist_Model = ArtistModel.ArtistModel()
#     return_value = artist_Model.delete()

    # assert return_value

def test_artists_post():


    name = ""
    birth_year = 1000
    death_year = 1100
    country = "korea"
    genre = "표현주의"
    return_json = artistController.post_artists(name, birth_year, death_year, country, genre)
    print(return_json)
    assert return_json['code'] == "NotInput"

    name = "현승재"
    birth_year = 1000
    death_year = 1100
    country = "12345678901234567890123456789012345678901234567890"
    genre = "표현주의"
    return_json = artistController.post_artists(name, birth_year, death_year, country, genre)
    print(return_json)
    assert return_json['code'] == "OutOfRangeInput"

    name = "현승재"
    birth_year = 1100
    death_year = 1000
    country = "korea"
    genre = "표현주의"

    return_json = artistController.post_artists(name, birth_year, death_year, country, genre)
    print(return_json)
    assert return_json['code'] == "WrongInput"


def test_artist_get():

    return_json = artistController.get_artist(None, 105)

    assert return_json['data']['name'] == "존 밀레이"
