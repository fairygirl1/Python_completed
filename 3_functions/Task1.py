"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""
a = int(input())#количество студентов

def beydg(name, group):
    print('Колледж Сириус')
    print("Имя: ", name)
    print('Группа: ', group)
for i in range (a):
    name = input()
    group = int(input())
    beydg(name, group)
print('Готово! Заберите бейджики.')