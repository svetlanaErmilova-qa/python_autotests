import requests
import json

token = '70f8852b73b31460c098e6f6d825b182'

''' Создание покемона '''
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    
    "name": "Света",
    "photo": "https://www.nicepng.com/png/full/62-622403_-.png"
})
response_pretty = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(response_pretty)

''' Смена имени покемона и его фото '''
response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 1469,
    "name": "Люся",
    "photo": "https://e7.pngegg.com/pngimages/979/917/png-clipart-pokemon-pokemon-thumbnail.png"
})
response_pretty1 = json.dumps(response_put.json(), indent=4, ensure_ascii=False)
print(response_pretty1)

''' Поймать покемона в покебол '''
response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token': token}, json={
    "pokemon_id": "1470"
})
response_pretty2 = json.dumps(response_post.json(), indent=4, ensure_ascii=False)
print(response_pretty2)

''' Выселить покемона из покебола '''
response_put_delete = requests.put('https://pokemonbattle.me:5000/trainers/deletePokebol', headers={'trainer_token': token}, json={
    "pokemon_id": "1471"
})
response_pretty3 = json.dumps(response_put_delete.json(), indent=4, ensure_ascii=False)
print(response_pretty3)
