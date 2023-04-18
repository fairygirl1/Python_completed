"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""

import sqlite3

conn = sqlite3.connect('library.sql')
c = conn.cursor()

reader_name = input('Введите свое имя: ')

def b_f_r (reader_name):

    c.execute("SELECT id FROM reader WHERE name=?", (reader_name,))
    reader_id = c.fetchone()[0]

    # Get all books associated with the reader
    c.execute("SELECT title, author FROM book WHERE id IN (SELECT book_id FROM reader_books WHERE reader_id=?)", (reader_id,))
    books = c.fetchall()



    if not books:
        print("No books found for this reader.")
    else:
        print(f"Books for {reader_name}:")
        for book in books:
            print(f"- {book[0]} by {book[1]}")

    conn.close()

