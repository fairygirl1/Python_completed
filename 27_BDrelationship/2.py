from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# создание базы данных в памяти
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

# определение модели Читатель
class Reader(Base):
    __tablename__ = 'reader'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book')

# определение модели Книга
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    reader_id = Column(Integer, ForeignKey('reader.id'))

# создание таблиц
Base.metadata.create_all(engine)

# создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# добавление данных в таблицы
reader1 = Reader(name='Анна')
reader2 = Reader(name='Иван')

book1 = Book(title='Мастер и Маргарита', author='Михаил Булгаков', reader_id=reader1.id)
book2 = Book(title='Преступление и наказание', author='Федор Достоевский', reader_id=reader1.id)
book3 = Book(title='Братья Карамазовы', author='Федор Достоевский', reader_id=reader2.id)

session.add_all([reader1, reader2, book1, book2, book3])
session.commit()


# функция для вывода всех книг для введенного с клавиатуры читателя
def get_books_by_reader_id(reader_id):
    reader = session.query(Reader).filter_by(id=reader_id).first()
    if reader is None:
        print(f'Читатель с id={reader_id} не найден')
    else:
        books = reader.books
        for book in books:
            print(f'"{book.title}" by {book.author}')

get_books_by_reader_id(1) # вывод всех книг для читателя с id=1
# "Мастер и Маргарита" by Михаил Булгаков
# "Преступление и наказание" by Федор Достоевский
