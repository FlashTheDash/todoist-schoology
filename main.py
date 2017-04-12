from pytodoist import todoist
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


def check_task(user, task_to_check, project_name='School'):
    '''
    returns True if the given task is already in todoist, else False
    '''
    project = user.get_project(project_name)
    tasks = []
    for task in project.get_tasks():
        tasks.append(task.content)
    if task_to_check in tasks:
        return True
    else:
        return False


def add_task(user, name, date, project_name='School'):
    '''
    adds a task to the specified todoist project
    '''
    project = user.get_project(project_name)
    project.add_task(name, date)


def update_tasks():
    user = todoist.login(credentials.todoist_username, credentials.todoist_password)
    events = get_events()
    for event in events:
        if not check_task(user, event.name):
            add_task(user, event.name, event.date)


if __name__ == "__main__":
    print('starting...')
    update_tasks()
    print('done...')
