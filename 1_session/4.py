'''
Напишите функцию, предлагающую пользователю ввести пароль пока пользователь не введет “off” и выводящую информацию о его надежности.
Надежным считается пароль, в котором больше 8 символов и есть хотя бы 1 буква в верхнем регистре.
Запустите функцию в отдельном потоке. Напишите функцию которая считает факториал числа 100000.
Запустите функцию в отдельном потоке, но только тогда когда пользователь закончит вводить пароли.
'''

from threading import Thread

def passw():
    pasw=input()
    while pasw != 'off':
        if len(pasw) > 8 and pasw.islower() == False:
            print('Пароль безопасен')
        else:
            print('Пароль небезопасен')
        pasw = input()

def fact():
    x = 1000
    result = 1
    for i in range(1, x+1):
        result = result*i
    print(result)

if __name__ == "__main__":
    thread_1 = Thread(target = passw)
    thread_2 = Thread(target = fact)
    thread_1.start()
    thread_1.join()
    thread_2.start()