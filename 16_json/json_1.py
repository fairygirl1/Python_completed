"""
Выведите из файла character.json Имя персонажа,
родную планету и список эпизодов, в которых он появлялся.
"""
import json

with open('character.json', 'r') as working:
    character = json.load(working)

print(character['name']['origin'][0]['episode'])
