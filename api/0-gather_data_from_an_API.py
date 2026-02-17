#!/usr/bin/python3
"""
Gather data from an API for a given employee ID and display
their TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{employee_id}"
    )

    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{employee_id}/todos"
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
        f"Employee {employee_name} is done with tasks"
        f"({number_done_tasks}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t {task.get('title')}")
