# pip install SQLAlchemy

"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

datab = "sqlite:///db_films.sql"
engine = create_engine(datab)


class Base(DeclarativeBase): pass 
#базовый класс для моделей

class Films(Base):
    __tablename__ = 'Films'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(String)
    genre = Column(String)
    rating = Column(Integer)

Base.metadata.create_all(bind=engine)

def create(fi_name, fi_date, fi_genre, fi_rating):
    with Session(autoflush=False, bind=engine) as bd:
        f = Films(name = fi_name, date = fi_date, genre = fi_genre, rating = fi_rating)
        bd.add(f)
        bd.commit()

create('КотикИ', '1985', 'Драма', '74')
create('Крокодильчики', '8754', 'Мелодрама', '10000')
create('Зайчики', '6740', 'Комедия', '41')
create('Курочки', '9378', 'Фантастика', '89')

def get_info():
    with Session(autoflush=False, bind=engine) as bd:
        f = bd.query(Films).all()
        for i in f:
            print(i.name)

def delete(id_del):
     with Session(autoflush=False, bind=engine) as bd:
        kill = bd.query(Films).filter(Films.id==id_del).first()
        bd.delete(kill)
        bd.commit()

delete(3)

