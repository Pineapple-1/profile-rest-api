import requests


TOKEN_ENDPOINT = 'https://mydjangoapiapp.herokuapp.com/login/'
PROFILE_ENDPOINT = 'https://mydjangoapiapp.herokuapp.com/profile/'

def get_token(email, password):
    """Retrieve the token for logging in user"""
    data = {'username': email, 'password': password}
    res = requests.post(TOKEN_ENDPOINT, data=data)

    return res.json()['token']


def get_profile(profile_id, token):
    """Retrive the profile for the logged in user"""
    url = '{}{}/'.format(PROFILE_ENDPOINT, profile_id)
    res = requests.get(url, headers={
        'Content-Type': 'application/json',
        'Authorization': 'Token {}'.format(token)
    })

    return res.json()

token = get_token('emial', 'password')
profile = get_profile(1, token)
print(profile)

