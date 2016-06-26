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
#     artist_Model = ArtistModel.ArtistModel()
#     return_value = artist_Model.delete()

    # assert return_value

