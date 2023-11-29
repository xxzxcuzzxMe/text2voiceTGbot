from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://username:password@localhost/db_name')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#Создание таблицы User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    voice_message_id = 
    voice_file_id =
    name = Column(String)
    message = Column(String)
    


Base.metadata.create_all(engine)
