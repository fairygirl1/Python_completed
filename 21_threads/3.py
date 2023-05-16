"""
Создайте функцию которая принимает путь до файла из папки files и 
меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""

import os
import threading
import time

def replace_string_in_file(file_path):
    try:
        # Чтение содержимого файла
        with open(file_path, 'r') as file:
            content = file.read()

        # Замена подстроки
        content = content.replace('ids', 'id')

        # Запись обновленного содержимого обратно в файл
        with open(file_path, 'w') as file:
            file.write(content)

        print(f"Файл {file_path} успешно обработан")
    except:
        print(f"Ошибка при обработке файла {file_path}")

if __name__ == '__main__':
    folder_path = 'Files'  # Путь до папки с файлами
    files = [f"file{i}.txt" for i in range(10)]  # Имена файлов

    start_time = time.time()

    # Создание и запуск потоков для каждого файла
    threads = []
    for file in files:
        file_path = os.path.join(folder_path, file)
        thread = threading.Thread(target=replace_string_in_file, args=(file_path,))
        thread.start()
        threads.append(thread)

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Время выполнения программы: {execution_time:.2f} сек")
