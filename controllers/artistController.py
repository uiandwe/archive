__author__ = 'hyeonsj'
from models import ArtistModel


def get_artists(filed, page):
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(filed)

    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(artist_list, int):
        #알 수 없는 컬럼일 경우
        if artist_list == 1054:
            return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': filed_list}

    json_data_list = []
    for item in artist_list:
        json_data_list.append(item.to_dict(item, filed_list))

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
        return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다." }

    if type(birth_year) is int and type(death_year) is int:
        if birth_year > death_year:
            return {'status': "400", 'code': "WrongInput", 'message': "파라미터의 값이 잘못되었습니다" }

    if len(name) > 45 or len(country) > 45 or len(genre) > 45:
        return {'status': "400", 'code': "OutOfRangeInput", 'message': "파라미터의 값이 최대 제한 범위를 넘었습니다" }

    artist = ArtistModel.ArtistModel().Artist()
    artist.name = name
    artist.birth_year = birth_year
    artist.death_year = death_year
    artist.country = country
    artist.genre = genre

    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.insert(artist)

    if type(return_value) is tuple:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': return_value[0], 'data': "", 'message': return_value[1]}

    artist_id = 0
    for artist_data in return_value:
        artist_id = artist_data[0]

    #insert 한 데이터 select
    instance_artist, filed_list = artist_model.get(None, artist_id)

    json_data = dict()
    for item in instance_artist:
        json_data = item.to_dict(item, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data, 'message': "success"}


def get_artist(filed, artist_id):
    artist_model = ArtistModel.ArtistModel()

    artist_list, filed_list = artist_model.get(filed, artist_id)

    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(artist_list, int):
        #알 수 없는 컬럼일 경우
        if artist_list == 1054:
            return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': filed_list}

    json_data_list = []
    for item in artist_list:
        json_data_list = item.to_dict(item, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data_list, 'message': "success"}


def delete_artists(artist_id):
    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.delete(artist_id)
    if return_value:
        return {'status': "200", 'code': 200, 'data': "", 'message': "삭제를 완료하였습니다."}
    else:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': "Forbidden", 'data': "", 'message': return_value[1]}