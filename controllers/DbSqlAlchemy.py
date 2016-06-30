__author__ = 'hyeonsj'
from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

host = config.host
user = config.user
passwd = config.passwd
db = config.db
charset = config.charset
engine = create_engine('mysql+pymysql://'+user+':'+passwd+'@'+host+'/'+db+'?charset=utf8', encoding='utf-8',
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import models
    Base.metadata.create_all(bind=engine)