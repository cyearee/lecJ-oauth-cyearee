
from requests_oauthlib import OAuth1Session
import secrets
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# this is like oauth-twitter but skipping ahead to step 4 bc you're just using your account (you as a user)

client_key = secrets.api_key
client_secret = secrets.api_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
data = json.loads(r.text)
print(data['statuses'][0]['user'].keys())
for status in data['statuses']:
	print('-------\n'+status['user']['screen_name']+'\n'+status['text']+'\n-------')