#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
from controllers import ControllerBase, InvalidController
from controllers.DbController import db_session
from models.models import Artist, Image


# /artists/:id/images get
def get_artist_images(artist_id, filed=None, page=None):
    # 해당 artist 이미지 데이터 가져오기
    data_dict = dict()

    image = Image()
    data_dict['images'] = image.find(None, artist_id)

    # 해당 artist 데이터 가져오기
    artist = Artist()
    data_dict['artist'] = artist.find(artist_id)

    return ControllerBase.success_return(data_dict)


# /artists/:id/images delete
def delete_artist_images(artist_id):

    db_session.query(Image).filter(Image.artist_id == artist_id).delete()
    db_session.commit()

    return ControllerBase.check_sql_delete_error(db_session)


# /artists/:id/images post
def post_artist_image(image_url, title, year, artist_id, description):
    # 파라미터 검사
    image_invalid = InvalidController.ImageInvalid()
    error_check = image_invalid.check_image_invalid(image_url, title, year, artist_id, description)
    if type(error_check) is dict:
        return error_check

     # insert 할 image 객체 생성
    image = Image()
    image_id = image.add(image_url, title, year, artist_id, description)

    # insert 한 데이터 select
    image_instance = image.find(image_id, None)

    return ControllerBase.success_return(image_instance)


# /artists/:id/images/:id get
def get_artist_image(artist_id, image_id, filed=None):
    # 해당 artist 이미지 데이터 가져오기
    data_dict = dict()

    image = Image()
    data_dict['images'] = image.find(image_id, None)

    # 해당 artist 데이터 가져오기
    artist = Artist()
    data_dict['artist'] = artist.find(artist_id)

    return ControllerBase.success_return(data_dict)


# /artists/:id/images/:id put
def put_artist_image(image_id, image_url, title, year, artist_id, description):
    # 파라미터 검사
    image_invalid = InvalidController.ImageInvalid()
    error_check = image_invalid.check_image_invalid(image_url, title, year, artist_id, description)
    if type(error_check) is dict:
        return error_check

    # 갱신할 image 객체 생성
    image = Image()
    image.update(image_id, image_url, title, year, artist_id, description)

    # 갱신된 객체 select
    image_instance = image.find(image_id, None)

    return ControllerBase.success_return(image_instance)


# /artists/:id/images/:id delete
def delete_artist_image(artist_id, image_id):
    db_session.query(Image).filter(Image.id == image_id).filter(Image.artist_id == artist_id).delete()
    db_session.commit()

    return ControllerBase.check_sql_delete_error(db_session)


# /images get
def get_images(filed=None, page=None):
    # 해당 artist 이미지 데이터 가져오기
    data_dict = dict()

    image = Image()
    image_instance = db_session.query(Image)
    image_dict = image.to_dict(image_instance)

    return ControllerBase.success_return(image_dict)


# /images delete
def delete_images():
    db_session.query(Image).delete()
    db_session.commit()

    return ControllerBase.check_sql_delete_error(db_session)


# /images/:id get
def get_image(image_id=None, filed=None):

    image = Image()
    image_instance = image.find(image_id, None)

    return ControllerBase.success_return(image_instance)


# /images/:id delete
def delete_image(image_id):
    db_session.query(Image).filter(Image.id == image_id).delete()
    db_session.commit()

    return ControllerBase.check_sql_delete_error(db_session)