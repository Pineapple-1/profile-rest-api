import requests 


TOKEN_ENDPOINT = 'http://localhost:8000/login/'
PROFILE_ENDPOINT = 'http://localhost:8000/profile/'
FEED_ENDPOINT = 'http://localhost:8000/feed/'


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

def get_feed():
    res = requests.get(FEED_ENDPOINT)
    return res.json()


feed = get_feed()
print(feed)


