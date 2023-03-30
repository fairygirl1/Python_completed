"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def param(a,b,c):
    if a != None or b != None or c != None:
        return a,b,c

a = input()
b = input()
c = input()
print(param(a,b,c))