'''
Напишите функцию которая с периодичностью в 2 секунды 
записывает в файл числа от 0 до 100 с шагом 3. 
Запустите функцию в потоке демоне, в основном потоке 
напишите бесконечный цикл который запрашивает у 
пользователя фамилии и заносит в список. Если введено 
слово off выводится список фамилий.
'''

from time import sleep
from threading import Thread

def write_nums():
    for num in range(0, 101, 3):
        with open('nums.txt', 'a+') as f:
            f.write(f'{num} ')
            sleep(2)

write_nums()

if __name__ == '__main__':
    thread_nums = Thread(target=write_nums, daemon=True)
    thread_nums.start()

    name = ''
    list_names = []
    while name != 'off':
        name = input("student's name: ")
        if name not in list_names and name != 'off':
            list_names.append(name)

    print(f"Student's list: {list_names}")
