"""
Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
Пример ввода: python file.py kakoitoArgument --name Oleg(Скрипт должен напечатать привет Oleg)
"""
import sys 

if len(sys.argv) == 1:
    print("hello world")

if "--name" in sys.argv:
     index_of_el = sys.argv.index("--name")
     print("hello",sys.argv[index_of_el+1])
