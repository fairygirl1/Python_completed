"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""
import sys
import os

if len(sys.argv) != 3:
    sys.exit(1)

text = sys.argv[1]
file_name = sys.argv[2]

file_text = os.path.join(text, file_name)
try:
    os.mkdir(file_text)
except OSError as e:
    print(f"не удалось создать файл: {e}")