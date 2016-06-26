#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
import pytest

from controllers.DbController import DbController
from controllers import ImageController
xfail = pytest.mark.xfail
dc = DbController()


def test_artist_images_get():

    return_json = ImageController.get_artist_images(102, None, None)
    print(return_json)
    assert len(return_json['data']['images']) == 4


# def test_artist_images_delete():
#
#     return_json = ImageController.delete_artist_images(102)
#     print(return_value)
#     assert return_json['code'] == 200