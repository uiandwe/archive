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


def test_artist_images_post():

    image_url = "test"
    title = "1111"
    year = "1985"
    artist_id = 100
    description = "현승재"
    print(image_url, title, year, artist_id, description)

    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)

    assert return_json['code'] == "NotInput"