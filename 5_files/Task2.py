"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""

with open('Еще один файл.txt', 'w+') as f:
    f.write('но у меня не получается')
    f.seek(0)
    a = f.read()
with open('File.txt') as f1:
    b = f1.read()
with open("Общий.txt", "w+") as f3:
    f3.write(b)
    f3.write(', ')
    f3.write(a)
    f3.seek(0)
    print(f3.read())