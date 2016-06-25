__author__ = 'hyeonsj'

#TODO
#디비 반환을 데이터가 아닌 객체로 반환하도록 수정하기


class artist():
    def __init__(self):
        self.id = 0
        self.name = None
        self.birth_year = 0
        self.death_year = 0
        self.country = None
        self.genre = None

    def get(self):
        return self
