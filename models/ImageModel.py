__author__ = 'hyeonsj'
from models.modelsBase import ModelsBase
from controllers import DbController
dc = DbController.DbController()


class ImageModel():

    class Image(ModelsBase):
        def __init__(self):
            self.id = 0
            self.image_url = ""
            self.title = ""
            self.year = 0
            self.artist_id = 0
            self.description = ""

    def get(self, filed=None, artist_id=None, image_id=None):

        filed_list = []

        #특정 필드가 아니면 artist테이블의 모든 칼럼 이름을 가져와서 filed_list에 넣음
        if filed is None or filed is '':
            filed = "*"
            sql = " SHOW COLUMNS FROM images; "
            cur = dc.exec(sql)

            for item in cur:
                filed_list.append(item[0])
        else:
            for item in filed.split(","):
                filed_list.append(item)

        sql = ""
        # /artists
        if artist_id is not None and image_id is None:
            sql = "SELECT "+filed+"  FROM images where artist_id = "+str(artist_id)

        # /aritsts/:id
        if image_id is not None and image_id > 0 and artist_id is None:
            sql = "SELECT "+filed+"  FROM images where id = "+str(image_id)

        # /artists/:id/images/:id
        if artist_id is not None and image_id is not None and image_id > 0:
            sql = "SELECT "+filed+"  FROM images as i, artists as a where a.id = i.artist_id and i.id = "+str(image_id)+\
                  " and a.id = "+str(artist_id)

        # /images
        if artist_id is None and image_id is None:
            sql = "SELECT "+filed+"  FROM images "

        # /images/:id
        if artist_id is None and image_id is not None:
            sql = "SELECT "+filed+"  FROM images where id = "+str(image_id)

        cur = dc.exec(sql)
        #에러일 경우 tuple 리턴
        if type(cur) is tuple:
            return cur

        return_instance_list = []
        for item in cur:
            #객체 생성 후 변수 삽입
            instance_artist = self.Image()

            for idx, column in enumerate(filed_list):
                instance_artist.set(instance_artist, column, item[idx])

            return_instance_list.append(instance_artist)

        return return_instance_list, filed_list

    def delete(self, artist_id=None, image_id=None):

        delete_and = ""

        if artist_id is not None and artist_id > 0 and image_id is not None:
            delete_and = " and id = "+str(image_id)+" "

        sql = "delete from images where artist_id = " + str(artist_id) + delete_and
        # /images
        if artist_id is None and image_id is None:
            sql = "delete from images "
        # /images/:id
        if artist_id is None and image_id > 0:
            sql = "delete from images where id = "+str(image_id)

        cur = dc.exec(sql)

        if type(cur) is tuple:
            return cur

        else:
            return True

    def insert(self, instance_image):

        mb = ModelsBase()
        insert_columns, insert_values = mb.insert_instance_to_str(instance_image)
        cur = mb.insert_exec("images", insert_columns, insert_values)

        return cur

    def update(self, instance_image, image_id):

        mb = ModelsBase()
        update_set_list = mb.update_instance_to_str(instance_image)
        cur = mb.update_exec("images", update_set_list, image_id)

        return cur