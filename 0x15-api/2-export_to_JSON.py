#!/usr/bin/python3
"""
Get tasks for user
"""
import json
import requests
import sys


def get_tasks_users(user_id):
    """Gets tasks for users"""
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


def g_json(d):
    """data to json"""
    user_id = d.get('user').get('id')
    username = d.get('user').get('username')
    task_info = []
    for task in data.get('tasks'):
        item = {}
        item['task'] = task.get('title')
        item['completed'] = task.get('completed')
        item['username'] = username
        task_info.append(item)
    task_json = {user_id: task_info}
    with open(str(user_id) + '.json', 'w') as f:
        json.dump(task_json, f)

if __name__ == '__main__':
    data = get_tasks_users(sys.argv[1])
    g_json(data)
