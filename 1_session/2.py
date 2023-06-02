'''
Напишите функцию которая высчитывает факториал 
числа, запустите функцию в отдельном процессе. 
В основной части программы запрашивайте числа пока 
пользователь не введет 0, числа добавляются в кортеж. 
После ввода 0 выведите сумму чисел в кортеже.
'''

from multiprocessing import Process, Pipe


def factorial(numbers, conn):
    if numbers == 1 or numbers == 0:
        conn.send(numbers)
    else:
        nums = 1
        for i in range(1, numbers + 1):
            nums = nums * i
        conn.send(nums)


if __name__ == '__main__':
    count = 0
    number = 1
    conn1, conn2 = Pipe()
    result = []
    while number != 0:
        number = int(input("Введите число: "))
        process = Process(target=factorial, args=(number, conn2))
        process.start()
        result.append(conn1.recv())

    for num in result:
        count = num + count
    # print(tuple(result))
    print(count)