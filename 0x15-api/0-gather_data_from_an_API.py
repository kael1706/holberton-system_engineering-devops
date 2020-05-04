#!/usr/bin/python3
"""
Get tasks for user
"""
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


def show_tasks(d):
    c_tasks = []
    for task in d.get('tasks'):
        if task.get('completed') is True:
            c_tasks.append(task)
    nc_tasks = len(c_tasks)
    t = len(d.get('tasks'))
    print('Employee ' +
          d.get('user').get('name') +
          ' is done with tasks({}/{}):'
          .format(
              nc_tasks,
              t))
    for task in c_tasks:
        print('\t ' + task['title'])

if __name__ == '__main__':
    data = get_tasks_users(sys.argv[1])
    show_tasks(data)
