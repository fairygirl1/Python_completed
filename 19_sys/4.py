"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""
import sys
import os

if len(sys.argv) != 2:
    sys.exit(1)

folder_name = sys.argv[1]

if not os.path.isfile(folder_name):
    sys.exit(1)

with open(folder_name) as f:
    for line in f:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        print(line)
        os.system(line)