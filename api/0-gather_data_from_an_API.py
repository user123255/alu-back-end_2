#!/usr/bin/python3
"""
Gather data from an API for a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(employee_id)
    )

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)

    done_tasks = [
        task for task in todos_data
        if task.get("completed") is True
    ]

    number_done_tasks = len(done_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_done_tasks,
            total_tasks
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
