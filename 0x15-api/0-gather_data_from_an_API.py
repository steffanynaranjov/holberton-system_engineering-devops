#!/usr/bin/python3
"""
Python script that using a REST API, for a given employee ID,
"""

if __name__ == '__main__':
    import requests
    import sys
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    us_id = requests.get(url + 'users?', params={'id': user_id}).json()
    to_do = requests.get(url + 'todos?', params={'userId': user_id}).json()

    EMPLOYEE = us_id[0].get('name')
    DONE = sum(tasks.get("completed")
               for tasks in to_do if tasks)
    TASK = len(to_do)
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE,
                                                          DONE,
                                                          TASK))
    [print("\t {}".format(task.get('title')))
     for task in to_do if task.get("completed")]
