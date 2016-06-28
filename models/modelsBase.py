__author__ = 'hyeonsj'
from controllers import DbController
dc = DbController.DbController()


class ModelsBase():

    def set(self, instance, column, value):
        setattr(instance, column, value)

    def to_dict(self, instance, filed_list):
        return_dict = dict()
        for filed in filed_list:
            return_dict[filed] = getattr(instance, filed)
        return return_dict

    # insert시 해당 class 객체의 파라미터를 sql문법에 맞게 변환시키는 함수
    # artist.name = tumblbug -> name , tumblbug로 뽑은 다음 -> insert into artists(name) values('tumblbug')로 변환
    def insert_instance_to_str(self, instance):
        # 해당 instance의 파라미터들을 dict 형태로 변환
        instance_dict = instance.__dict__

        columns_list = []
        values_list = []
        columns = instance_dict.keys()

        for item in columns:
            # id의 경우 삽입, 갱신이 불가능하므로 제외
            if item is not "id":
                if instance_dict[item] is not None and instance_dict[item] != "":
                    columns_list.append(item)
                    # 타입이 문자열일 경우 앞뒤로 ''를 붙여준다.
                    if type(instance_dict[item]) is str:
                        values_list.append("'"+instance_dict[item]+"'")
                    else:
                        values_list.append(str(instance_dict[item]))

        str_columns = ",".join(columns_list)
        str_values = ",".join(values_list)

        return str_columns, str_values

    # update시 해당 class 객체의 파라미터를 sql문법에 맞게 변환시키는 함수
    # artist.name = tumblbug -> name , tumblbug로 뽑은 다음 -> update artists set name = 'tumblbug' 로 변환
    def update_instance_to_str(self, instance):
        instance_dict = instance.__dict__
        update_set_list = []
        columns = instance_dict.keys()
        for item in columns:
            if item is not "id":
                if type(instance_dict[item]) is str:
                    update_set_list.append(item+"='"+instance_dict[item]+"'")
                else:
                    update_set_list.append(item+"="+str(instance_dict[item]))

        update_set_list = ",".join(update_set_list)
        return update_set_list

    # model들의 insert문
    def insert_exec(self, table_name, insert_columns, insert_values):

        sql = "insert into "+table_name+"("+insert_columns+") value("+insert_values+")"
        dc.exec(sql)

        sql = "SELECT LAST_INSERT_ID();"
        cur = dc.exec(sql)

        return cur

    # model들의 update문
    def update_exec(self, table_name, update_values, table_id):
        sql = "update "+table_name+" set "+update_values+" where id ="+str(table_id)
        cur = dc.exec(sql)
        return cur
