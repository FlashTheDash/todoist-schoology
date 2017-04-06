import todoist
import requests
from requests_oauthlib import OAuth1
import datetime
import credentials


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date


def get_events():
    '''
    returns a list of Event objects that are scheduled from today forward
    '''
    # create OAuth key
    oauth = OAuth1(client_key=credentials.schoology_client_key, client_secret=credentials.schoology_client_secret, signature_type='auth_header')

    # create headers for requests
    headers = {'Accept': 'application/json',
               'Host': 'api.schoology.com',
               }

    url = 'https://api.schoology.com/v1/users/{}/events'.format(credentials.schoology_user_id)
    today = str(datetime.date.today())
    parameters = {'start_date': today}

    # send get request to specified URL with params and everything
    # requests is great!
    r = requests.get(url, headers=headers, auth=oauth, params=parameters)
    events_list = r.json()['event']

    events = []

    for event in events_list:
        event_name = event['title']
        event_date = event['start']
        events.append(Event(event_name, event_date))

    return events


# docs: https://developer.todoist.com/#read-resources
