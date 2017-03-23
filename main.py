import todoist
import requests
from requests_oauthlib import OAuth1


# a bunch of constants that I'll port into another file eventually
user_id = '24163835'
client_key = '3f370efb5e18b1e0f664e55bf4ab014a058d31b65'
client_secret = '4ea251c386d021a01cd18937e357951c'
todoist_token = '914638fdc19f19e4c1aabc7fb8d8d0158e823a66'


# the functions that can pull data from schoology


# create OAuth key
oauth = OAuth1(client_key=client_key, client_secret=client_secret, signature_type='auth_header')

# create headers for requests
headers = {'Accept': 'application/json',
           'Host': 'api.schoology.com',
           }


def show_events():
    url = 'https://api.schoology.com/v1/users/{}/events?start=0&limit=500'.format(user_id)

    # send get request to specified URL
    r = requests.get(url, headers=headers, auth=oauth)
    # events = r.json()['event']
    #
    # for event in events:
    #     print(event['title'], '\n   ', event['start'])
    print(r.json())

show_events()



# the functions that push data to todoist
# docs: https://developer.todoist.com/#read-resources
