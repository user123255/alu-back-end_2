#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress using a REST API.
"""
import requests
import sys


def gather_data():
    """Fetches and displays employee progress."""
    if len(sys.argv) < 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks using multi-line list comprehension for PEP8
    completed_tasks = [
        task.get("title") for task in todos_data if task.get("completed")
    ]
    total_tasks = len(todos_data)
    done_count = len(completed_tasks)

    # Print summary header
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_count, total_tasks
    ))

    # Print completed task titles
    for title in completed_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    gather_data()
