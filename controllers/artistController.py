#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
from controllers import ControllerBase, InvalidController
from controllers.DbController import db_session
from models.models import Artist


# /artists get
def get_artists(filed, page):
    artist = Artist()
    artist_query = db_session.query(Artist)
    artist_list = artist.to_dict(artist_query)

    return ControllerBase.success_return(artist_list)


# /artists delete
def delete_all_artists():

    db_session.query(Artist).delete()
    db_session.commit()

    return ControllerBase.check_sql_delete_error(db_session)


# /artists post
def post_artists(name, birth_year=None, death_year=None, country=None, genre=None):

    # 파라미터 검사
    artist_invalid = InvalidController.ArtistInvalid()
    error_check = artist_invalid.check_artist_invalid(name, birth_year, death_year, country, genre)
    if type(error_check) is dict:
        return error_check
    # insert 할 artist 객체 생성
    artist = Artist()
    artist_id = artist.add(name, birth_year, death_year, country, genre)

    # insert 한 데이터 select
    artist_query = db_session.query(Artist).filter(Artist.id == artist_id)
    artist_instance = artist.to_dict(artist_query)

    return ControllerBase.success_return(artist_instance)


# /artists/:id get
def get_artist(filed, artist_id):

    artist = Artist()
    artist_query = db_session.query(Artist).filter(Artist.id == artist_id)
    artist_list = artist.to_dict(artist_query)

    return ControllerBase.success_return(artist_list)


# /artists/:id delete
def delete_artists(artist_id):
    db_session.query(Artist).filter(Artist.id == artist_id).delete()
    db_session.commit()

    return ControllerBase.check_sql_delete_error(db_session)


# /artists/:id put
def put_artist(artist_id, name=None, birth_year=None, death_year=None, country=None, genre=None):

    # 파라미터 검사
    artist_invalid = InvalidController.ArtistInvalid()
    error_check = artist_invalid.check_artist_invalid(name, birth_year, death_year, country, genre)
    if type(error_check) is dict:
        return error_check

    # 갱신할 artist 객체 생성
    artist = Artist()
    artist.update(artist_id, name, birth_year, death_year, country, genre)

    # 갱신된 객체 select
    artist_query = db_session.query(Artist).filter(Artist.id == artist_id)
    artist_list = artist.to_dict(artist_query)

    return ControllerBase.success_return(artist_list)