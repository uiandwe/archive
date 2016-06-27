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


def delete_artist_images(artist_id, image_id=None):
    image_model = ImageModel.ImageModel()
    return_value = image_model.delete(artist_id, image_id)
    if return_value:
        return {'status': "200", 'code': 200, 'data': "", 'message': "삭제를 완료하였습니다."}
    else:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': "Forbidden", 'data': "", 'message': return_value[1]}


def post_artist_image(image_url, title, year, artist_id, description):

    if image_url is None or image_url == "" or title is None or title == "" or year is None \
            or year == "" or artist_id is None or artist_id == "" or description is None or description == "":
        return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다."}

    if len(image_url) > 255 or len(title) > 255 or len(description) > 255:
        return {'status': "400", 'code': "OutOfRangeInput", 'message': "파라미터의 값이 최대 제한 범위를 넘었습니다"}

    # fk인 artist_id의 값이 artists 테이블에 있는지 확인
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(None, artist_id)
    if len(artist_list) <= 0:
        return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다."}

    image = ImageModel.ImageModel().Image()
    image.image_url = image_url
    image.title = title
    image.year = year
    image.artist_id = artist_id
    image.description = description

    image_model = ImageModel.ImageModel()
    return_value = image_model.insert(image)

    if type(return_value) is tuple:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': return_value[0], 'data': "", 'message': return_value[1]}

    image_id = 0
    for image_data in return_value:
        image_id = image_data[0]

    # insert 한 데이터 select
    instance_image, filed_list = image_model.get(None, None, image_id)

    json_data = dict()
    for item in instance_image:
        json_data = item.to_dict(item, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data, 'message': "success"}


def get_artist_image(artist_id, image_id, filed=None):
    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(filed, artist_id, image_id)

    #해당 하는 데이터가 없다면 에러 코드 리턴
    if len(image_list) <= 0:
        return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': "잘못된 파라미터 요청입니다."}

    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(image_list, int):
        #알 수 없는 컬럼일 경우
        if image_list == 1054:
            return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': filed_list}

    json_image = dict()
    for item in image_list:
        json_image = item.to_dict(item, filed_list)
    data_dict = dict()
    data_dict['images'] = json_image

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


def put_artist_image(image_id, image_url, title, year, artist_id, description):

    if image_url is None or image_url == "" or title is None or title == "" or year is None \
            or year == "" or artist_id is None or artist_id == "" or description is None or description == "":
        return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다."}
    if float(year) is False:
        return {'status': "400", 'code': "InvalidInput", 'message': "파라미터의 데이터형이 맞지 않습니다."}
    if len(image_url) > 255 or len(title) > 255 or len(description) > 255:
        return {'status': "400", 'code': "OutOfRangeInput", 'message': "파라미터의 값이 최대 제한 범위를 넘었습니다"}

    # fk인 artist_id의 값이 artists 테이블에 있는지 확인
    artist_model = ArtistModel.ArtistModel()
    artist_list, filed_list = artist_model.get(None, artist_id)
    if len(artist_list) <= 0:
        return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다."}

    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(None, artist_id, image_id)

    #해당 하는 데이터가 없다면 에러 코드 리턴
    if len(image_list) <= 0:
        return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': "잘못된 파라미터 요청입니다."}

    image = ImageModel.ImageModel().Image()
    image.image_url = image_url
    image.title = title
    image.year = year
    image.artist_id = artist_id
    image.description = description

    image_model = ImageModel.ImageModel()
    return_value = image_model.update(image, image_id)

    if type(return_value) is tuple:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': return_value[0], 'data': "", 'message': return_value[1]}

    # insert 한 데이터 select
    instance_image, filed_list = image_model.get(None, None, image_id)

    json_data = dict()
    for item in instance_image:
        json_data = item.to_dict(item, filed_list)

    return {'status': "200", 'code': 200, 'data': json_data, 'message': "success"}


def get_images(filed=None, page=None):
    image_model = ImageModel.ImageModel()
    image_list, filed_list = image_model.get(filed, None, None)
    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(image_list, int):
        #알 수 없는 컬럼일 경우
        if image_list == 1054:
            return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': filed_list}
    json_data_list = []
    for item in image_list:
        json_data_list.append(item.to_dict(item, filed_list))

    return {'status': "200", 'data': json_data_list, 'message': "success"}


def delete_images():
    image_model = ImageModel.ImageModel()
    return_value = image_model.delete()
    if return_value:
        return {'status': "200", 'code': 200, 'data': "", 'message': "삭제를 완료하였습니다."}
    else:
        if isinstance(return_value[0], int):
            return {'status': "403", 'code': "Forbidden", 'data': "", 'message': return_value[1]}