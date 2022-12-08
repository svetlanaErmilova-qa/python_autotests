import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200


def test_piece_of_body():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id': '1238'})
    assert response.json()['trainer_name'] == 'Зверь'


@pytest.mark.parametrize('key, value', [('trainer_name', 'Зверь'), ('city', 'Москва')])

def test_parameters_body(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id': '1238'})
    assert response.json()[key] == value