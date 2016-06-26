#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
import pytest

from controllers.DbController import DbController
from models import ArtistModel
xfail = pytest.mark.xfail
dc = DbController()


def test_artist_count():
    filed = "name"
    page = 0
    artist_Model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_Model.get(filed)

    assert len(artist_list) == 50

    assert artist_list[0].name == "빈센트 반 고흐"


# def test_delete_all_artists():
#     from models import ArtistModel
#     a = ArtistModel.ArtistModel()
#     filed = ''
#     return_instance_artist_list = a.get(filed)
    # for temp in return_instance_artist_list:
    #     print(temp.id, temp.name, temp.birth_year, temp.death_year, temp.country, temp.genre)

    # return_json = artistController.delete_all_artists(dc)
    #
    # assert return_json['status'] == "200"
    #
    # sql = "select count(*) from artists;"
    # cur = dc.find(sql)
    # for temp_count in cur:
    #     assert temp_count[0] == 0
