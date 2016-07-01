#-*- coding: utf-8 -*-
import pytest

from controllers import ImageController
xfail = pytest.mark.xfail


def test_artist_images_get():

    return_json = ImageController.get_artist_images(102, None, None)
    # print(return_json)
    assert return_json['data']['artist']['name'] == '빈센트 반 고흐'

#
# def test_artist_images_delete():
#
#     return_json = ImageController.delete_artist_images(103)
#     print(return_json)
#     assert return_json['code'] == 200


def test_artist_images_post():

    image_url = "1"
    title = "2"
    year = 1000
    artist_id = 100
    description = "Test"

    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    assert return_json['code'] == "NotInput"

    image_url = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    # print(return_json)
    assert return_json['code'] == "OutOfRangeInput"

    image_url = ""
    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    # print(return_json)
    assert return_json['code'] == "NotInput"

    image_url = "1"
    year = "1000"
    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    # print(return_json)
    assert return_json['code'] == "NotInput"


def test_artist_image_get():
    return_json = ImageController.get_artist_image(102, 1, None)
    assert return_json['data']['images']['title'] == '밤의 카페 테라스'

@xfail
def test_artist_image_get():

    return_json = ImageController.get_artist_image(102, 2, None)
    # print(return_json)

    assert return_json['data']['images']['title'] == '동심원들과 정사각형들'


def test_artist_image_delete():

    return_json = ImageController.delete_artist_image(102, 77)
    # print(return_json)
    assert return_json['code'] == 200


def test_artist_image_put():

    image_id = 74
    title = "2"
    year = 1000
    artist_id = 103
    description = "Test"
    image_url = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    assert return_json['code'] == "OutOfRangeInput"

    image_url = ""
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    assert return_json['code'] == "NotInput"

    image_id = 74
    year = image_id
    image_url = "74"
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)

    assert return_json['data']['year'] == 74


def test_images_get():

    return_json = ImageController.get_images()
    assert return_json['data'][0]['artist_id'] == 102


def test_images_post():

    image_url = "1"
    title = "2"
    year = 1000
    artist_id = 100
    description = "Test"

    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    assert return_json['code'] == "NotInput"

    image_url = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
                "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    # print(return_json)
    assert return_json['code'] == "OutOfRangeInput"

    image_url = ""
    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    # print(return_json)
    assert return_json['code'] == "NotInput"

    image_url = "1"
    year = "1000"
    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    # print(return_json)
    assert return_json['code'] == "NotInput"

    year = 1000
    artist_id = 103
    return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)
    # print(return_json)

    assert return_json['data']['year'] == 1000


# def test_images_delete():
#     return_json = ImageController.delete_images()
#     print(return_json)
#     assert return_json['code'] == 200


def test_image_get():

    return_json = ImageController.get_image(1, None)
    # print(return_json)
    assert return_json['data']['artist_id'] == 102


def test_artist_image_put():

    return_json = ImageController.get_images()

    image_id = return_json['data'][-1]['id']
    image_url = "1"
    title = "2"
    year = 1000
    artist_id = 102
    description = "Test"

    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    assert return_json['code'] == "UnknownFiled"

    artist_id = 103
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
    year = "year"
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    print(return_json)
    assert return_json['code'] == "InvalidInput"

    artist_id = 103
    year = 1001
    return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)
    print(return_json)

    assert return_json['data']['year'] == 1001


# def test_images_delete():
#     return_json = ImageController.get_images()
#
#     image_id = return_json['data'][-1]['id']
#
#     return_json = ImageController.delete_image(image_id)
#     print(return_json)
#     assert return_json['code'] == 200