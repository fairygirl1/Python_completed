"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""

import threading
import queue
import os

def process_names_queue(names_queue, output_folder):
    while not names_queue.empty():
        name = names_queue.get()
        file_path = os.path.join(output_folder, name + ".txt")
        create_file(file_path)

def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write("This is a new file created at {}".format(file_path))
        print("File created:", file_path)

if __name__ == '__main__':
    names_queue = queue.Queue()
    output_folder = "output_task3"

    # Чтение имен из файла Names.txt
    with open("names.txt", 'r') as file:
        names = file.read().splitlines()

    # Заполнение очереди именами в виде путей до файлов
    for name in names:
        names_queue.put(name)

    # Создание папки для хранения файлов
    os.makedirs(output_folder, exist_ok=True)

    # Создание пула потоков
    threads = []

    # Запуск потоков для обработки очереди имен
    for _ in range(3):
        thread = threading.Thread(target=process_names_queue, args=(names_queue, output_folder))
        thread.start()
        threads.append(thread)

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    print("All files created.")
