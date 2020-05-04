#!/usr/bin/python3
"""
data to csv
"""
import csv
import request
import sys


def get_tasks_users(user_id):
    """Gets Tasks for users"""
    url = 'https://jsonplaceholder.typicode.com/'
    params1 = {'id': user_id}
    employe = requests.get(url + 'users',
                           params=params1,
                           verify=False).json()
    params2 = {'userId': user_id}
    tasks = requests.get(url + 'todos',
                         params=params2,
                         verify=False).json()
    r = {'user': employe[0], 'tasks': tasks}
    return r


def gcsv(d):
    """data to csv"""
    with open(sys.argv[1] + '.csv', 'w') as f:
        pencil = csv.writer(f, quoting=csv.QUOTE_ALL)
        user_id = data.get('user').get('id')
        username = d.get('user').get('username')
        for entry in d.get('tasks'):
            pencil.writerow([
                user_id,
                username,
                entry.get('completed'),
                entry.get('title'),
            ])


if __name__ == '__main__':
    data = get_tasks_users(sys.argv[1])
    gcsv(data)
