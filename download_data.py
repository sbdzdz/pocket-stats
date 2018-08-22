import configparser
import json
import pocket
from pocket import Pocket

# uri = 'https://example.com'
# token = Pocket.get_request_token(consumer_key=key, redirect_uri=uri)
# auth_url = Pocket.get_auth_url(code=token, redirect_uri=uri)
# user_credentials = Pocket.get_credentials(consumer_key=key, code=token)
# access_token = user_credentials['access_token']

config = configparser.ConfigParser()
config.read('config.ini')
consumer_key = config['POCKET']['CONSUMER_KEY']
access_token = config['POCKET']['ACCESS_TOKEN']

api = pocket.Pocket(consumer_key, access_token)
data = api.get(state='all')[0]['list']

with open('data/list.json', 'w') as f:
    json.dump(data, f)
