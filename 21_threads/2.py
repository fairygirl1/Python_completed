"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать 
"Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код 
неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""

import threading
import time

def bomb_message():
    while True:
        print("Вводите быстрее")
        time.sleep(3)

def defuse_bomb():
    correct_code = "12345"  # Верный код от бомбы

    bomb_thread = threading.Thread(target=bomb_message)
    bomb_thread.daemon = True  # Установка потока в режим демона
    bomb_thread.start()

    user_code = input("Введите код от бомбы: ")

    if user_code == correct_code:
        print("Бомба разминирована")
    else:
        print("Вы взорвались")

if __name__ == '__main__':
    defuse_bomb()
