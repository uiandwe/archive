#-*- coding: utf-8 -*-
import pytest

from controllers.DbController import DbController
from controllers import ImageController
xfail = pytest.mark.xfail
dc = DbController()

@xfail
def test_artist_images_get():

    return_json = ImageController.get_artist_images(103, None, None)
    print(return_json)
    assert len(return_json['data']['images']) == 5


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


def test_artist_image_get():

    return_json = ImageController.get_artist_image(103, 2, None)
    print(return_json)

    assert return_json['data']['images']['title'] == '동심원들과 정사각형들'

@xfail
def test_artist_image_get():

    return_json = ImageController.get_artist_image(102, 2, None)
    print(return_json)

    assert return_json['data']['images']['title'] == '동심원들과 정사각형들'


def test_artist_image_delete():

    return_json = ImageController.delete_artist_images(103, 70)
    print(return_json)
    assert return_json['code'] == 200


def test_artist_image_put():

    image_id = 70
    image_url = "1"
    title = "2"
    year = 1000
    artist_id = 103
    description = "Test"

    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    assert return_json['code'] == "UnknownFiled"

    image_url = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    print(return_json)
    assert return_json['code'] == "OutOfRangeInput"

    image_url = ""
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    print(return_json)
    assert return_json['code'] == "NotInput"

    image_url = "1"
    year = "1000"
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    print(return_json)
    assert return_json['code'] == "UnknownFiled"


    image_id = 73
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    print(return_json)

    assert return_json['data']['year'] == 1000





