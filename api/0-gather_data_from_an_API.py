#!/usr/bin/python3
"""
Gather data from an API for a given employee ID and display
their TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    # Check if employee ID is provided
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_done_tasks = len(done_tasks)

    # Print progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        number_done_tasks,
        total_tasks
    ))

    # Print completed task titles
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
