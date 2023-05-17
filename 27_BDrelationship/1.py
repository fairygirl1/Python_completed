"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Определение модели Читатель
class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="reader")

# Определение модели Книга
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    reader_id = Column(Integer, ForeignKey('readers.id'))
    reader = relationship("Reader", back_populates="books")

# Создание базы данных
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Создание нового читателя и добавление его в базу данных
new_Maxim = Reader(name="Максим")
session.add(new_Maxim)
new_Kirill = Reader(name="Кирилл")
session.add(new_Kirill)
session.commit()

# Создание новой книги и добавление ее в базу данных для указанного читателя
new_book = Book(title="Алые паруса", author="Александр Грин", reader=new_Maxim)
session.add(new_book)
new_book1 = Book(title="Вино из одуванчиков", author="Рэй Брэдбери", reader=new_Maxim)
session.add(new_book1)
new_book2 = Book(title="Оно", author="Стивен Кинг", reader=new_Kirill)
session.add(new_book2)
new_book3 = Book(title="Вишневый сад", author="Антон Чехов", reader=new_Kirill)
session.add(new_book3)
session.commit()

# Функция для вывода всех книг для заданного читателя
def get_books_for_reader(reader_name):
    reader = session.query(Reader).filter_by(name=reader_name).first()
    if reader:
        books = reader.books
        if books:
            for book in books:
                print(f"Название: {book.title}, Автор: {book.author}")
        else:
            print("У читателя нет книг.")
    else:
        print("Читатель не найден.")

# Пример использования функции
reader_name = input("Введите имя читателя: ")
get_books_for_reader(reader_name)


