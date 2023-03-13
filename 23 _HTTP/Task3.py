"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех 
персонажей, начиная с вашего номера в журнале и заканчивая 
ваш номер*5
Сохраните в .json файл.
"""

import requests
import json 

characters_data= []

for i in range(18,21):
    r = requests.get(f"https://rickandmortyapi.com/api/character/{i}").json()

    name = r['name']
    planet = r['origin']['name']
    episode = [episode.split('/')[-1] for episode in r['episode']]
    character_data = {'name':name, 'planet':planet, 'episodes':episode}
    characters_data.append(character_data)

    result = '\n'.join(str(line) for line in characters_data)

with open('characters.json', 'w') as f:
    json.dump(result, f)
    
    
    