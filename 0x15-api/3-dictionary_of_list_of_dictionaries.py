#!/usr/bin/python3
"""
Get tasks for all users
"""
import requests
import json


def get_tasks_users():
    """Gets tasks for all users"""
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users',
                         verify=False).json()
    tasks = requests.get(url + 'todos',
                         verify=False).json()
    r = {}
    for user in users:
        user_info = []
        for task in tasks:
            if user.get('id') == task.get('userId'):
                d = {}
            d['task'] = task.get('title')
            d['completed'] = task.get('completed')
            d['username'] = user.get('username')
            user_info.append(d)
        r[user.get('id')] = user_info
    return r


if __name__ == '__main__':
    with open('todo_all_employees.json', 'w') as f:
        json.dump(get_tasks_users(), f)
