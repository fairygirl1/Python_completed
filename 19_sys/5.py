"""
Напишите скрипт который в качестве параметра из командной строки 
принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""

import sys
import subprocess

# Проверка наличия аргумента с именем файла
if len(sys.argv) < 2:
    print("Имя файла не указано.")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        # Чтение команд из файла и выполнение
        for line in file:
            command = line.strip()
            if command:
                subprocess.run(command, shell=True)
except FileNotFoundError:
    print("Файл не найден.")
    sys.exit(1)
except Exception as e:
    print("Ошибка при выполнении команд:", e)
    sys.exit(1)
