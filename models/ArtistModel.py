__author__ = 'hyeonsj'
from controllers import DbController, artistController
dc = DbController.DbController()


class ArtistModel():

    class Artist():
        def __init__(self):
            self.id = 0
            self.name = ""
            self.birth_year = 0
            self.death_year = 0
            self.country = ""
            self.genre = ""

        def set(self, instance, column, value):
            setattr(instance, column, value)

        def to_dict(self, instance, filed_list):
            return_dict = dict()
            for filed in filed_list:
                return_dict[filed] = getattr(instance, filed)
            return return_dict

    def get(self, filed):

        filed_list = []

        #특정 필드가 아니면 artist테이블의 모든 칼럼 이름을 가져와서 filed_list에 넣음
        if not filed:
            filed = "*"
            sql = " SHOW COLUMNS FROM artists; "
            cur = dc.find(sql)

            for item in cur:
                filed_list.append(item[0])
        else:
            for item in filed.split(","):
                filed_list.append(item)

        sql = "SELECT "+filed+"  FROM artists "
        cur = dc.find(sql)
        #에러일 경우 tuple 리턴
        if type(cur) is tuple:
            return cur

        return_instance_list = []
        for item in cur:
            #객체 생성 후 변수 삽입
            instance_artist = self.Artist()

            for idx, column in enumerate(filed_list):
                instance_artist.set(instance_artist, column, item[idx])

            return_instance_list.append(instance_artist)

        return return_instance_list, filed_list

    def delete(self, artist_id=None):

        delete_where = ""

        if artist_id:
            delete_where = "where id = "+str(artist_id)+" "

        sql = "delete from artists " + delete_where
        cur = dc.delete(sql)

        if type(cur) is tuple:
            return cur

        else:
            return True