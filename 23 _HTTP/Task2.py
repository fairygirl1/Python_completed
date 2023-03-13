"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests

r = requests.get("https://randomuser.me/api/").json()

a = r['results'][0]

name = a['name']['first']
# print(name)

country = a['location']['country']
# print(country)

phone = a['phone']
print(name, ',', country, ',', phone)