__author__ = 'hyeonsj'
from models import ArtistModel, ImageModel
from controllers import ControllerBase, InvalidController


def get_artist_images(artist_id, filed=None, page=None):
    #  해당 artist의 이미지 가져오기
    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(filed, artist_id, None)

    error_check = ControllerBase.check_sql_error(image_list, filed_list)
    if type(error_check) is dict:
        return error_check

    data_dict = dict()
    data_dict['images'] = ControllerBase.sql_to_dict(image_list, filed_list)

    # 해당 artist의 정보가져오기
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(filed, artist_id)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    data_dict['artist'] = ControllerBase.sql_to_dict(artist_list, filed_list)

    return {'status': "200", 'data': data_dict, 'message': "success"}


def delete_artist_images(artist_id, image_id=None):
    image_model = ImageModel.ImageModel()
    return_value = image_model.delete(artist_id, image_id)

    return ControllerBase.check_sql_delete_error(return_value)


def post_artist_image(image_url, title, year, artist_id, description):
    # 파라미터 검사
    image_invalid = InvalidController.ImageInvalid()
    error_check = image_invalid.check_image_invalid(image_url, title, year, artist_id, description)
    if type(error_check) is dict:
        return error_check

    image = ImageModel.ImageModel().Image()
    image.image_url = image_url
    image.title = title
    image.year = year
    image.artist_id = artist_id
    image.description = description

    image_model = ImageModel.ImageModel()
    return_value = image_model.insert(image)
    # insert한 데이터의 id
    image_id = 0
    for item in return_value:
        image_id = item[0]

    # insert 한 데이터 select
    instance_image, filed_list = image_model.get(None, None, image_id)
    json_data = ControllerBase.sql_to_dict(instance_image, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data, 'message': "success"}


# /artists/:id/images/:id get
def get_artist_image(artist_id, image_id, filed=None):
    # 해당 image 데이터 가져오기
    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(filed, artist_id, image_id)

    error_check = ControllerBase.check_sql_error(image_list, filed_list)
    if type(error_check) is dict:
        return error_check

    data_dict = dict()
    data_dict['images'] = ControllerBase.sql_to_dict(image_list, filed_list)

    # 해당 artist 데이터 가져오기
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(filed, artist_id)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    data_dict['artist'] = ControllerBase.sql_to_dict(artist_list, filed_list)

    return {'status': "200", 'data': data_dict, 'message': "success"}


# /artists/:id/images/:id put
def put_artist_image(image_id, image_url, title, year, artist_id, description):
    # 파라미터 검사
    image_invalid = InvalidController.ImageInvalid()
    error_check = image_invalid.check_image_invalid(image_url, title, year, artist_id, description)
    if type(error_check) is dict:
        return error_check

    # image 객체 생성 및 갱신
    image = ImageModel.ImageModel().Image()
    image.image_url = image_url
    image.title = title
    image.year = year
    image.artist_id = artist_id
    image.description = description

    image_model = ImageModel.ImageModel()
    return_value = image_model.update(image, image_id)

    check_update_error = ControllerBase.check_sql_update_error(return_value)
    if check_update_error is tuple:
        return check_update_error

    # insert 한 데이터 select
    instance_image, filed_list = image_model.get(None, None, image_id)
    json_data = ControllerBase.sql_to_dict(instance_image, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data, 'message': "success"}


def get_images(filed=None, page=None):
    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(filed, None, None)

    error_check = ControllerBase.check_sql_error(image_list, filed_list)
    if type(error_check) is dict:
        return error_check

    json_data_list = ControllerBase.sql_to_dict(image_list, filed_list)

    return {'status': "200", 'data': json_data_list, 'message': "success"}


def delete_images():
    image_model = ImageModel.ImageModel()
    return_value = image_model.delete()
    return ControllerBase.check_sql_delete_error(return_value)


def get_image(image_id, filed=None):
    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(filed, None, image_id)

    error_check = ControllerBase.check_sql_error(image_list, filed_list)
    if type(error_check) is dict:
        return error_check

    json_data_list = ControllerBase.sql_to_dict(image_list, filed_list)

    return {'status': "200", 'data': json_data_list, 'message': "success"}


def delete_image(image_id):
    image_model = ImageModel.ImageModel()
    return_value = image_model.delete(None, image_id)
    return ControllerBase.check_sql_delete_error(return_value)