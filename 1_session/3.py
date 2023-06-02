"""
Напишите функцию принимающую список строк и ширину окна.
Функция должна выводить на экран новый список в котором к 
каждой строке добавлено определенное количество пробелов
так чтобы строка оказалась в центре окна. Для расчета 
пробелов есть формула (len(s) – w) // 2.
Если строка больше или равна ширине окна добавляем ее 
в список в прежнем виде.
Запустите функцию в отдельном процессе. В основном 
процессе раз в 2 секунды выводится фраза
“я еще думаю” пока пользователь не выполнит остановку 
скрипта нажатием ctrl+c.
"""

from multiprocessing import Process
from time import sleep


def screen(list_string, width):
    new_list = []
    for string in list_string:
        if len(string) <= width:
            cunt_append = abs((len(string) - width) // 2)
            string = (cunt_append * "*") + string + (cunt_append * "*")
            print(string)
            # with open("screen.txt", "a") as file:
            #     file.write(string + "\n")
            new_list.append(string)
        else:
            print(string)
            new_list.append(string)
    return new_list


pr = Process(target=screen, args=(["sakfr", "daun", "dd"], 5))
pr.start()

while True:
    try:
        print('Я еще думаю')
        sleep(2)
    except KeyboardInterrupt:
        break