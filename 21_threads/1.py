"""
Создайте функцию напоминалку в отдельном потоке от основной программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку 
в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading
import time

def reminder():
    reminder_text = input("О чем вам напомнить? ")
    reminder_time = int(input("Через сколько секунд напомнить? "))

    time.sleep(reminder_time)
    print(f"Напоминание: {reminder_text}")

if __name__ == '__main__':
    reminder_thread = threading.Thread(target=reminder)
    reminder_thread.start()

    time.sleep(10)  # Задержка в 10 секунд

