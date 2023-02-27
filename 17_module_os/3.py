"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os

os.chdir(r'/home/sasha/study/python/modules_OS')
os.mkdir("target")

for i in range (1, 11):
    os.chdir(r'/home/sasha/study/python/modules_OS/target')
    i = str(i)
    text_file = open(f"{i}", "w")
    i = int(i)
    i += 1

name = 'xaxaxa'
number = 0
spisok = os.listdir(r'/home/sasha/study/python/modules_OS/target')
for n in spisok:
    n = int(n)
    if n%2 == 0:
        y = str(n)
        name_file = name + y
        os.rename(f"{n}", f"{name_file}")
       
      
        # name_file = name
