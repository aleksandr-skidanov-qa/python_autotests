import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '98921146b0fb988d803413a31473ff30'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '38992'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get_name = requests.get(url = f'{URL}/trainers', headers=HEADER, params = {'trainer_id':TRAINER_ID})
    assert response_get_name.json()["data"][0]["trainer_name"] == "Alex"

