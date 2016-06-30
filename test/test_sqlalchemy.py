__author__ = 'hyeonsj'
import pytest

from controllers.DbSqlAlchemy import init_db
xfail = pytest.mark.xfail


def test_connect():
    init_db()

    from controllers.DbSqlAlchemy import db_session
    from models.models import User, Image, Artist

    artist_query = db_session.query(Artist).filter(Artist.id==103)
    print(artist_query)
    entries = [dict(name=artist.name, email=artist.id) for artist in artist_query]
    print(entries)