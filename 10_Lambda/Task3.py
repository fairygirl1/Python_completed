#Напишите список функций по требованию. Пользователь вводит имя.
#Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
#Если на О,Ь,Л,Н. То добавляется "Сверхразум".
# Если ни на одну из этих букв то добавляется "Просто" перед именем.

def name(n):
    let =  n[-1]
    if let == 'А' or let == 'Я' or let == 'Г' or let == 'М':
        gen = lambda n, genius: print(n, genius)
        gen(n, 'ГЕНИЙ')
    elif let == 'О' or let == 'Ь' or let == 'Л' or let == 'Н':
        gen = lambda n, mind: print(n, mind)
        gen(n, 'СВЕРХРАЗУМ')
    else:
        gen = lambda just,n: print(just, n)
        gen('ПРОСТО', n)
n = input("What's your name? ").swapcase()

name(n)
