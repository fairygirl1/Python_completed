"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""

def HEX(cvet, n, **kwargs):
    print(f'{cvet}: {n}')
    for i in kwargs:
        print(f'{i}: {kwargs[i]}')


HEX(input(), int(input()), синий = 123, красный = 23, белый = 4)