__author__ = 'hyeonsj'
from models import ArtistModel
from controllers import ControllerBase, InvalidController


# /artists get
def get_artists(filed, page):
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(filed)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    json_data_list = ControllerBase.sql_to_dict(artist_list, filed_list)

    return ControllerBase.success_return(json_data_list)


# /artists delete
def delete_all_artists():
    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.delete()
    return ControllerBase.check_sql_delete_error(return_value)


# /artists post
def post_artists(name, birth_year=None, death_year=None, country=None, genre=None):

    # 파라미터 검사
    image_invalid = InvalidController.ImageInvalid()
    error_check = image_invalid.check_artist_invalid(name, birth_year, death_year, country, genre)
    if type(error_check) is dict:
        return error_check

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

    return ControllerBase.success_return(json_data)


# /artists/:id get
def get_artist(filed, artist_id):
    artist_model = ArtistModel.ArtistModel()

    artist_list, filed_list = artist_model.get(filed, artist_id)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    json_data_list = ControllerBase.sql_to_dict(artist_list, filed_list)

    return ControllerBase.success_return(json_data_list)


# /artists/:id delete
def delete_artists(artist_id):
    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.delete(artist_id)
    return ControllerBase.check_sql_delete_error(return_value)


# /artists/:id put
def put_artist(artist_id, name=None, birth_year=None, death_year=None, country=None, genre=None):

    # 파라미터 검사
    image_invalid = InvalidController.ImageInvalid()
    error_check = image_invalid.check_artist_invalid(name, birth_year, death_year, country, genre)
    if type(error_check) is dict:
        return error_check

    #해당 artist_id 데이터가 있는지 확인
    artist_model = ArtistModel.ArtistModel()

    artist_list, filed_list = artist_model.get(None, artist_id)

    error_check = ControllerBase.check_sql_error(artist_list, filed_list)
    if type(error_check) is dict:
        return error_check

    artist = ArtistModel.ArtistModel().Artist()
    artist.name = name
    artist.birth_year = birth_year
    artist.death_year = death_year
    artist.country = country
    artist.genre = genre

    return_value = artist_model.update(artist, artist_id)
    check_update_error = ControllerBase.check_sql_update_error(return_value)
    if check_update_error is tuple:
        return check_update_error

    # update 한 데이터 select
    instance_artist, filed_list = artist_model.get(None, artist_id)

    json_data = ControllerBase.sql_to_dict(instance_artist, filed_list)

    return ControllerBase.success_return(json_data)