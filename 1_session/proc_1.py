"""
Напишите 2 функции, одна считает сумму четных чисел, 
вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 
1000000
"""

import multiprocessing

def chet(start, end, queue):
    sum_chet = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sum_chet += i
    queue.put(sum_chet)

def nechet(start, end, queue):
    sum_nechet = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            sum_nechet += i
    queue.put(sum_nechet)

if __name__ == '__main__':
    start = 1
    end = 99

    queue = multiprocessing.Queue()

    chet_proc = multiprocessing.Process(target=chet, args=(start, end, queue))
    nechet_proc = multiprocessing.Process(target=nechet, args=(start, end, queue))

    chet_proc.start()
    chet_proc.join()

    nechet_proc.start()
    nechet_proc.join()

    chet = queue.get()
    nechet = queue.get()

    print('Сумма четных чисел = ', chet)
    print('Сумма нечетных чисел = ', nechet)