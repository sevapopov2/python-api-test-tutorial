'''An API testing exercise to test reqres.in API.'''

import requests

def test_get_list_of_users():
    '''Get list of users with an API.'''
    URL = 'https://reqres.in/api/users'
    response = requests.get(URL)
    assert response.status_code == 200
