__author__ = 'hyeonsj'
from models import ArtistModel


def get_artists(filed, page):
    artist_Model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_Model.get(filed)

    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(artist_list, int):
        #알 수 없는 컬럼일 경우
        if artist_list == 1054:
            return {'status': "400", 'data': "", 'message': filed_list}

    json_data_list = []
    for item in artist_list:
        json_data_list.append(item.to_dict(item, filed_list))

    return {'status': "200", 'data': json_data_list, 'message': "success"}


def delete_all_artists(dc):
    return {'status': "200", 'data': "", 'message': "success"}