'''
Напишите функцию которая с периодичностью в 2 секунды 
записывает в файл числа от 0 до 100 с шагом 3. 
Запустите функцию в потоке демоне, в основном потоке 
напишите бесконечный цикл который запрашивает у 
пользователя фамилии и заносит в список. Если введено 
слово off выводится список фамилий.
'''

import multiprocessing
import time

def tofile (start, end, file_name, step, conn):
    for i in (start - int(step), end + 1):
        i = i + int(step)

        parent_conn.send(i)
        parent_conn.close()



if __name__ == '__main__':
    start = 0
    end = 100
    step = 3
    file_name = 'numbers.txt'


    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(target=tofile, args=(start, end, file_name, step, child_conn), daemon=True)
    process.start()
    
