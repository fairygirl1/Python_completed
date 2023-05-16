import multiprocessing

def sum_even_numbers(start, end, result_queue):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    result_queue.put(total)

def sum_odd_numbers(start, end, result_queue):
    total = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            total += num
    result_queue.put(total)

if __name__ == '__main__':
    start = 1
    end = 99

    # Создаем очередь для передачи результатов
    result_queue = multiprocessing.Queue()

    # Создаем два процесса для подсчета сумм четных и нечетных чисел
    even_process = multiprocessing.Process(target=sum_even_numbers, args=(start, end, result_queue))
    odd_process = multiprocessing.Process(target=sum_odd_numbers, args=(start, end, result_queue))

    # Запускаем процессы
    even_process.start()
    odd_process.start()

    # Ждем завершения процессов
    even_process.join()
    odd_process.join()

    # Получаем результаты сумм из очереди
    even_sum = result_queue.get()
    odd_sum = result_queue.get()

    print("Сумма четных чисел:", even_sum)
    print("Сумма нечетных чисел:", odd_sum)
