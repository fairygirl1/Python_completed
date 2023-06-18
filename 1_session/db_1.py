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

base = declarative_base()

class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    books_list = relationship('Book', back_populates='reader')

class Book(Base):
    __tablename__ = 'books'
    
