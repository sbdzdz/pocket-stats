import configparser
import json
import pocket
from pocket import Pocket

config = configparser.ConfigParser()
config.read('config.ini')
consumer_key = config['POCKET']['CONSUMER_KEY']
access_token = config['POCKET']['ACCESS_TOKEN']

api = pocket.Pocket(consumer_key, access_token)
data = api.get(state='all')[0]['list']

with open('data/list.json', 'w') as f:
    json.dump(data, f)
