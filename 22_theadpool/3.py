"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off 
для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен 
с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите 
функции в разных потоках.
"""

import threading
import queue

def add_students_to_queue(queue):
    while True:
        surname = input("Введите фамилию студента (или 'off' для завершения): ")
        if surname == "off":
            break
        queue.put(surname)

def process_students_queue(queue):
    while True:
        surname = queue.get()
        if surname == "off":
            queue.put(surname)  # Возвращаем 'off' в очередь для завершения других потоков
            break
        print(f"Студент {surname} отчислен")

if __name__ == '__main__':
    students_queue = queue.Queue()

    # Запуск потока для добавления студентов в очередь
    add_thread = threading.Thread(target=add_students_to_queue, args=(students_queue,))
    add_thread.start()

    # Запуск потока для обработки очереди студентов
    process_thread = threading.Thread(target=process_students_queue, args=(students_queue,))
    process_thread.start()    

    # Ожидание завершения потоков
    add_thread.join()
    process_thread.join()

    print("Программа завершена")
