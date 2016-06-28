__author__ = 'hyeonsj'
from models import ArtistModel, ImageModel


class ImageInvalid():

    def check_image_invalid(self, image_url, title, year, artist_id, description):
        if image_url is None or image_url == "" or title is None or title == "" or year is None or year == "" \
                or artist_id is None or artist_id == "" or description is None or description == "":
            return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다."}

        if float(year) is False:
            return {'status': "400", 'code': "InvalidInput", 'message': "파라미터의 데이터형이 맞지 않습니다."}

        if len(image_url) > 255 or len(title) > 255 or len(description) > 255:
            return {'status': "400", 'code': "OutOfRangeInput", 'message': "파라미터의 값이 최대 제한 범위를 넘었습니다."}

        # fk인 artist_id의 값이 artists 테이블에 있는지 확인
        artist_model = ArtistModel.ArtistModel()
        artist_list, filed_list = artist_model.get(None, artist_id)
        if len(artist_list) <= 0:
            return {'status': "400", 'code': "NotInput", 'message': "파라미터의 데이터가 없습니다."}

        return True