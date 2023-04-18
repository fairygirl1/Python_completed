import chardet

# определяем кодировку файла
with open('/home/sashas-toy/study/Python_completed/26_Databases/SQL_modules/bin/python /home/sashas-toy/study/Python_completed/28_sockets/1_server.py', 'rb') as f:
    result = chardet.detect(f.read())
    
# выводим определенную кодировку
print(result['encoding'])

# открываем файл с определенной кодировкой
with open('/home/sashas-toy/study/Python_completed/26_Databases/SQL_modules/bin/python /home/sashas-toy/study/Python_completed/28_sockets/1_server.py', encoding=result['encoding']) as f:
    # здесь код для работы с файлом


