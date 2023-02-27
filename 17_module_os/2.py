"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""
import os
os.chdir(r'/home/sasha/study/python/modules_OS')
os.mkdir("papka")

for i in range (1, 11):
    os.chdir(r'/home/sasha/study/python/modules_OS/papka')
    os.mkdir(f"{i}")
    i += 1