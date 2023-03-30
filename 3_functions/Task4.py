"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

weight = int(input("Ваш вес: "))
height = int(input("Ваш рост: "))
def amount_imt():
    index = weight // (height * height)
    return index
def set_imt():
    imt = amount_imt()
    if imt <= 18.5:
        return 'недостаточный вес'
    elif 18.5 < imt < 25:
        return 'ИМТ в норме'
    else:
        return 'избыточный вес'
print('У вас ', set_imt())