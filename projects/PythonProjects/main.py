import requests
URL='https://api.pokemonbattle.ru/v2'
TOKEN='98921146b0fb988d803413a31473ff30'
HEADER={'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_registration={
    "trainer_token": TOKEN,
    "email": "skidans777@yandex.ru",
    "password": "Samara163!!"
}
body_confirmation ={
    "trainer_token": "токен_из_бота_котика"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER , json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER , json = body_confirmation)
print(response_confirmation.text)'''

body_create = {
    "name": "Бульба",
    "photo_id": 5
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json =body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)



body_new_name = {
    "pokemon_id": "461476",
    "name": "пика",
    "photo_id": -1
}
response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json =body_new_name)
print(response_new_name.text)



body_pokeball ={
    "pokemon_id": "461476"
}
response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json =body_pokeball)
print(response_pokeball.text)
