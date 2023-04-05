import sqlite3
import hashlib

# Подключаемся к базе данных
conn = sqlite3.connect('users.sql')
c = conn.cursor()

# Создаем таблицу пользователей, если ее еще нет
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT)''')

# Предлагаем пользователю зарегистрироваться или авторизироваться
action = input("Do you want to register (R) or login (L)? ").lower()

if action == 'r':  # Регистрация нового пользователя
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Создаем хэш пароля
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Добавляем нового пользователя в базу данных
    c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    print('Account successfully created')

elif action == 'l':  # Авторизация пользователя
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Получаем хэш пароля для указанного пользователя
    c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if result is None:
        print("Invalid username or password")
    else:
        password_hash = result[0]
        # Проверяем соответствие хэша пароля
        if hashlib.sha256(password.encode('utf-8')).hexdigest() == password_hash:
            print("Login successful")
        else:
            print("Invalid username or password")

conn.close()

