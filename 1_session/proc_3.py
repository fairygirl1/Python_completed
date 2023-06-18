"""
Напишите функцию которая через канал обмена 
возвращает количество валюты которую можно приобрести на 
n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее 
данные задержкой в 0.5 секунды 
передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import multiprocessing
import time

def converter(n, conn):
    result = n * 75
    conn.send(result)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()  

    n_1 = 15
    n_2 = 30  

    process_1 = multiprocessing.Process(target=converter, args=(n_1, child_conn))
    process_1.start()
    time.sleep(0.5)
    print(parent_conn.recv())

    process_2 = multiprocessing.Process(target=converter, args=(n_2, child_conn))    
    process_2.start()
    time.sleep(0.5)
    print(parent_conn.recv())

    
    

