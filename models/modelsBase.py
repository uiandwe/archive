#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
from controllers.DbController import db_session


class ModelsBase():

    def db_insert(self, instance):
        db_session.add(instance)
        db_session.commit()

        return self.db_last_id()

    def db_update(self, instance):

        db_session.add(instance)
        db_session.commit()

        return instance

    def db_last_id(self):
        sql = "SELECT LAST_INSERT_ID();"
        sql_last_id = db_session.execute(sql)
        last_id = 0
        for item in sql_last_id:
            last_id = item[0]
        return last_id

    def len_check(self, instance_list):
        if len(instance_list) > 1:
            return instance_list
        else:
            return instance_list[0]


