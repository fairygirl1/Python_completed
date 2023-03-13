"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests

# r = requests.get("https://cataas.com/cat")
# with open ("cat_1.jpg", "wb") as cat_1:
#            #открыть на запись в бинарном режиме
#             cat_1.write(r.content)

# r2 = requests.get("https://cataas.com/cat")
# with open ("cat_2.jpg", "wb") as cat_2:
#             cat_2.write(r2.content)

# r3 = requests.get("https://cataas.com/cat?type=or")
# with open ("cat_or_1.png", "wb") as cat_3:
#             cat_3.write(r3.content)

# r4 = requests.get("https://cataas.com/cat?type=or")
# with open ("cat_or_2.png", "wb") as cat_4:
#             cat_4.write(r4.content)

r5 = requests.get("https://cataas.com/cat?filter=pixel")
with open ("cat_pi_1.png", "wb") as cat_5:
            cat_5.write(r5.content)

r6 = requests.get("https://cataas.com/cat?filter=pixel")
with open ("/home/sashas-toy/study/completed/23_HTTP/cat_pi_2.png", "wb") as cat_6:
            cat_6.write(r6.content)