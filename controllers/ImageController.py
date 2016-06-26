__author__ = 'hyeonsj'
from models import ArtistModel, ImageModel


def get_artist_images(artist_id, filed=None, page=None):
    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(filed, artist_id, None)

    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(image_list, int):
        #알 수 없는 컬럼일 경우
        if image_list == 1054:
            return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': filed_list}

    json_data_list = []
    for item in image_list:
        json_data_list.append(item.to_dict(item, filed_list))
    data_dict = dict()
    data_dict['images'] = json_data_list

    artist_model = ArtistModel.ArtistModel()

    artist_list, filed_list = artist_model.get(filed, artist_id)

    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(artist_list, int):
        #알 수 없는 컬럼일 경우
        if artist_list == 1054:
            return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': filed_list}

    for item in artist_list:
        data_dict['artist'] = item.to_dict(item, filed_list)

    return {'status': "200", 'data': data_dict, 'message': "success"}


def delete_all_artists():
    artist_model = ArtistModel.ArtistModel()
    return_value = artist_model.delete()
    if return_value:
        return {'status': "200", 'data': "", 'message': "삭제를 완료하였습니다."}
    else:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': "Forbidden", 'data': "", 'message': return_value[1]}
