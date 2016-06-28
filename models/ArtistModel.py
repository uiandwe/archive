__author__ = 'hyeonsj'
from models.modelsBase import ModelsBase
from controllers import DbController
dc = DbController.DbController()


class ArtistModel():

    class Artist(ModelsBase):
        def __init__(self):
            self.id = 0
            self.name = ""
            self.birth_year = 0
            self.death_year = 0
            self.country = ""
            self.genre = ""

    def get(self, filed=None, artist_id=None):

        filed_list = []

        #특정 필드가 아니면 artist테이블의 모든 칼럼 이름을 가져와서 filed_list에 넣음
        if filed is None or filed is '':
            filed = "*"
            sql = " SHOW COLUMNS FROM artists; "
            cur = dc.exec(sql)

            for item in cur:
                filed_list.append(item[0])
        else:
            for item in filed.split(","):
                filed_list.append(item)

        sql = "SELECT "+filed+"  FROM artists "

        if artist_id is not None:
            sql += " where id = "+str(artist_id)

        cur = dc.exec(sql)
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
        cur = dc.exec(sql)

        if type(cur) is tuple:
            return cur

        else:
            return True

    def insert(self, instance_artist):
        mb = ModelsBase()
        insert_columns, insert_values = mb.insert_instance_to_str(instance_artist)

        cur = mb.insert_exec("artists", insert_columns, insert_values)
        print(cur)
        return cur

    def update(self, instance_artist, artist_id):
        mb = ModelsBase()
        update_set_list = mb.update_instance_to_str(instance_artist)

        cur = mb.update_exec("artists", update_set_list, artist_id)

        return cur