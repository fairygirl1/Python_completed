import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задаем IP-адрес сервера и порт для подключения
server_ip = '127.0.0.1'
server_port = 12345

# Подключаемся к серверу
client_socket.connect((server_ip, server_port))
print("Подключение к серверу установлено.")

# Запрашиваем название файла у пользователя
file_name = input("Введите название файла: ")

# Отправляем название файла серверу
client_socket.send(file_name.encode())

# Получаем количество слов от сервера
word_count = client_socket.recv(1024).decode()
print("Количество слов в файле:", word_count)

# Закрываем соединение
client_socket.close()
