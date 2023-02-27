""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

os.mkdir(r'/home/sasha/study/python/modules_OS/task4')
os.chdir(r'/home/sasha/study/python/modules_OS/task4')
file = open("answer.txt", "w")
file.write('я не выполнила заание, и вообще я лентяйка!')
file.close()