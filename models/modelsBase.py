__author__ = 'hyeonsj'


class ModelsBase():

    def set(self, instance, column, value):
        setattr(instance, column, value)

    def to_dict(self, instance, filed_list):
        return_dict = dict()
        for filed in filed_list:
            return_dict[filed] = getattr(instance, filed)
        return return_dict