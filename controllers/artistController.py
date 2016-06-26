__author__ = 'hyeonsj'
from models import ArtistModel


def get_artists(filed, page):
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(filed)

    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(artist_list, int):
        #알 수 없는 컬럼일 경우
        if artist_list == 1054:
            return {'status': "400", 'data': "", 'message': filed_list}

    json_data_list = []
    for item in artist_list:
        json_data_list.append(item.to_dict(item, filed_list))

    return {'status': "200", 'data': json_data_list, 'message': "success"}


def delete_all_artists():
    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.delete()
    if return_value:
        return {'status': "200", 'data': "", 'message': "success"}
    else:
        if isinstance(return_value[0], int):
            return {'status': "403", 'data': "", 'message': return_value[1]}