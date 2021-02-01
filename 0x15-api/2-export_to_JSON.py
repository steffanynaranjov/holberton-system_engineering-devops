#!/usr/bin/python3
"""
Python script that using a REST API, for a given employee ID,
"""

if __name__ == '__main__':
    import sys
    import json
    import requests
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    us_id = requests.get(url + 'users?', params={'id': user_id}).json()
    to_do = requests.get(url + 'todos?', params={'userId': user_id}).json()
    employee = us_id[0].get("username")

    with open("{}.json".format(user_id), "w") as jsonf:
        json.dump({user_id: [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": employee} for task in to_do]}, jsonf)
