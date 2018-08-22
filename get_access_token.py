import configparser
import urllib
import requests
import webbrowser

def get_request_token(consumer_key, redirect_uri):
    url = 'https://getpocket.com/v3/oauth/request'
    params = {'consumer_key': consumer_key, 'redirect_uri': redirect_uri }
    headers = {'X-Accept': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    request_token = response.json()['code']
    return request_token

def authenticate_in_browser(request_token, redirect_uri):
    url = "https://getpocket.com/auth/authorize"
    params = {'request_token': request_token, 'redirect_uri': redirect_uri}
    webbrowser.open(url + '?' + urllib.parse.urlencode(params))

def get_access_token(consumer_key, request_token):
    url = 'https://getpocket.com/v3/oauth/authorize'
    params = {'consumer_key': consumer_key, 'code': request_token}
    headers = {'X-Accept': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    access_token = response.json()['access_token']
    return access_token

if __name__ == '__main__':
    redirect_uri = 'https://sebastiandziadzio.com'
    config = configparser.ConfigParser()
    config.read('config.ini')
    consumer_key = config['POCKET']['CONSUMER_KEY']

    request_token = get_request_token(consumer_key, redirect_uri)
    authenticate_in_browser(request_token, redirect_uri)
    input('Please hit Enter once you authorize the app in the browser')
    access_token = get_access_token(consumer_key, request_token)

    config.set('POCKET', 'ACCESS_TOKEN', access_token)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
