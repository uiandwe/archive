__author__ = 'hyeonsj'

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from controllers.DbController import Base, db_session
from .modelsBase import ModelsBase


class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    birth_year = Column(Integer)
    death_year = Column(Integer)
    country = Column(String(45))
    genre = Column(String(45))

    def __init__(self, name=None, birth_year=0, death_year=0, country=None, genre=None):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.country = country
        self.genre = genre

    def to_dict(self, instance_list):
        mb = ModelsBase()
        artist_list = [dict(id=artist.id, name=artist.name, birth_year=artist.birth_year, death_year=artist.death_year,
                            country=artist.country, genre=artist.genre) for artist in instance_list]
        return mb.len_check(artist_list)

    def add(self, name=None, birth_year=0, death_year=0, country=None, genre=None):
        artist = Artist(name, birth_year, death_year, country, genre)
        mb = ModelsBase()
        return mb.db_insert(artist)

    def update(self, artist_id, name=None, birth_year=0, death_year=0, country=None, genre=None):
        artist = db_session.query(Artist).filter(Artist.id == artist_id).one()
        artist.name = name
        artist.birth_year = birth_year
        artist.death_year = death_year
        artist.country = country
        artist.genre = genre

        mb = ModelsBase()
        return mb.db_update(artist)

    def find(self, artist_id=0):
        artist = Artist()

        if artist_id > 0:
            artist_query = db_session.query(Artist).filter(Artist.id == artist_id)
        else:
            artist_query = db_session.query(Artist)
        return artist.to_dict(artist_query)


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(255))
    title = Column(String(255))
    year = Column(Integer)
    artist_id = Column(Integer, ForeignKey('artists.id', ondelete="CASCADE"))
    description = Column(String(255))

    def __init__(self, image_url=None, title=None, year=0, artist_id=0, description=None):
        self.image_url = image_url
        self.title = title
        self.year = year
        self.artist_id = artist_id
        self.description = description

    def to_dict(self, instance_list):
        image_list = [dict(id=image.id, image_url=image.image_url, title=image.title, year=image.year,
                           artist_id=image.artist_id, description=image.description) for image in instance_list]
        mb = ModelsBase()
        return mb.len_check(image_list)

    def add(self, image_url=None, title=None, year=0, artist_id=0, description=None):
        image = Image(image_url, title, year, artist_id, description)
        mb = ModelsBase()
        return mb.db_insert(image)

    def update(self, image_id, image_url=None, title=None, year=0, artist_id=0, description=None):

        image = db_session.query(Image).filter(Image.id == image_id).one()
        image.image_url = image_url
        image.title = title
        image.title = title
        image.year = year
        image.artist_id = artist_id
        image.description = description

        mb = ModelsBase()
        return mb.db_update(image)

    def find(self, image_id, artist_id):
        image = Image()
        if artist_id is None and image_id > 0:
            image_query = db_session.query(Image).filter(Image.id == image_id)
        if image_id is None and artist_id > 0:
            image_query = db_session.query(Image).filter(Image.artist_id == artist_id)
        if image_id is None and artist_id is None:
            image_query = db_session.query(Image)
        return image.to_dict(image_query)