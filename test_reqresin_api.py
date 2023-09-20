'''An API testing exercise to test reqres.in API.'''

import requests


def test_get_list_of_users():
    '''Get list of users with an API.'''
    URL = 'https://reqres.in/api/users'
    response = requests.get(URL)
    assert response.status_code == 200


def test_create_new_user():
    '''Create new user with API.'''
    URL = 'https://reqers.in/api/users'
    data = {
        'name': 'Vsevolod Popov',
        'movies': ['Live until Monday', 'Where is nophelet located?']
    }
    response = requests.post(URL, data=data)
    assert response.status_code == 200
