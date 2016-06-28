__author__ = 'hyeonsj'
from models import ArtistModel
from controllers import ControllerBase


def get_artists(filed, page):
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(filed)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    json_data_list = ControllerBase.sql_to_dict(artist_list, filed_list)

    return {'status': "200", 'data': json_data_list, 'message': "success"}


def delete_all_artists():
    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.delete()
    if return_value:
        return {'status': "200", 'data': "", 'message': "삭제를 완료하였습니다."}
    else:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': "Forbidden", 'data': "", 'message': return_value[1]}


def post_artists(name, birth_year=None, death_year=None, country=None, genre=None):

    if name is None or name == "":
        return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다."}

    if type(birth_year) is int and type(death_year) is int:
        if birth_year > death_year:
            return {'status': "400", 'code': "WrongInput", 'message': "파라미터의 값이 잘못되었습니다"}

    if len(name) > 45 or len(country) > 45 or len(genre) > 45:
        return {'status': "400", 'code': "OutOfRangeInput", 'message': "파라미터의 값이 최대 제한 범위를 넘었습니다"}

    artist = ArtistModel.ArtistModel().Artist()
    artist.name = name
    artist.birth_year = birth_year
    artist.death_year = death_year
    artist.country = country
    artist.genre = genre

    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.insert(artist)

    artist_id = 0
    for artist_data in return_value:
        artist_id = artist_data[0]

    # insert 한 데이터 select
    instance_artist, filed_list = artist_model.get(None, artist_id)

    json_data = ControllerBase.sql_to_dict(instance_artist, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data, 'message': "success"}


def get_artist(filed, artist_id):
    artist_model = ArtistModel.ArtistModel()

    artist_list, filed_list = artist_model.get(filed, artist_id)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    json_data_list = ControllerBase.sql_to_dict(artist_list, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data_list, 'message': "success"}


def delete_artists(artist_id):
    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.delete(artist_id)
    if return_value:
        return {'status': "200", 'code': 200, 'data': "", 'message': "삭제를 완료하였습니다."}
    else:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': "Forbidden", 'data': "", 'message': return_value[1]}


def update_artist(artist_id, name=None, birth_year=None, death_year=None, country=None, genre=None):

    if type(birth_year) is int and type(death_year) is int:
        if birth_year > death_year:
            return {'status': "400", 'code': "WrongInput", 'message': "파라미터의 값이 잘못되었습니다"}

    if len(name) > 45 or len(country) > 45 or len(genre) > 45:
        return {'status': "400", 'code': "OutOfRangeInput", 'message': "파라미터의 값이 최대 제한 범위를 넘었습니다"}

    #해당 artist_id 데이터가 있는지 확인
    artist_model = ArtistModel.ArtistModel()

    artist_list, filed_list = artist_model.get(None, artist_id)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    if len(artist_list) == 0:
        return {'status': "404", 'code': "ResourceNotFound", 'data': "", 'message': "리소스를 찾을 수 없습니다."}

    artist = ArtistModel.ArtistModel().Artist()
    artist.name = name
    artist.birth_year = birth_year
    artist.death_year = death_year
    artist.country = country
    artist.genre = genre

    return_value = artist_model.update(artist, artist_id)

    if type(return_value) is tuple:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': return_value[0], 'data': "", 'message': return_value[1]}

    # update 한 데이터 select
    instance_artist, filed_list = artist_model.get(None, artist_id)

    json_data = ControllerBase.sql_to_dict(instance_artist, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data, 'message': "success"}