"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""

import threading
import queue

def print_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print(f"Divisors of {number}: {divisors}")

def process_queue(queue):
    while not queue.empty():
        number = queue.get()
        print_divisors(number)

if __name__ == '__main__':
    numbers_queue = queue.Queue()
    numbers = [10, 20, 30, 40, 50]

    for number in numbers:
        numbers_queue.put(number)

    pool = []

    for _ in range(3):
        thread = threading.Thread(target=process_queue, args=(numbers_queue,))
        thread.start()
        pool.append(thread)

    for thread in pool:
        thread.join()

    print("All tasks completed.")
