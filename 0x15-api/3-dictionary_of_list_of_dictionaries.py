#!/usr/bin/python3
"""
Python script that using a REST API, for a given employee ID,
"""

if __name__ == '__main__':
    import json
    import requests
    url = 'https://jsonplaceholder.typicode.com/'
    us_id = requests.get(url + "users").json()

    dict = {}
    for user in us_id:
        dict[user.get("id")] = [{"username": user.get("username"),
                                 "task": task.get("title"),
                                 "completed": task.get("completed")}
            for task in requests.get(url + "todos",
                                    params={"userId": user.get("id")}).json()]

    with open("todo_all_employees.json", "w", newline="") as json_f:
        json.dump(dict, json_f)
