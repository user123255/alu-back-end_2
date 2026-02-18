#!/usr/bin/env python3
"""
0-gather_data_from_an_API.py
Fetches TODO list progress for a given employee ID.
"""

import sys
import requests


def get_employee_todos(employee_id):
    """Fetch employee info and TODOs, then print completed tasks."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = (
        f"{base_url}/users/{employee_id}"
    )
    todos_url = (
        f"{base_url}/todos?userId={employee_id}"
    )

    # Get employee info
    user_resp = requests.get(user_url)
    if user_resp.status_code != 200:
        print(
            f"Error fetching user with ID {employee_id}"
        )
        return

    employee = user_resp.json()
    employee_name = employee.get(
        "name", "Unknown"
    )

    # Get todos
    todos_resp = requests.get(todos_url)
    if todos_resp.status_code != 200:
        print(
            f"Error fetching todos for user ID {employee_id}"
        )
        return

    todos = todos_resp.json()
    total_tasks = len(todos)
    done_tasks = [
        t for t in todos if t.get("completed")
    ]

    # Print output in the required format
    header = (
        f"Employee {employee_name} is done with tasks("
        f"{len(done_tasks)}/{total_tasks})"
    )
    print(header + ":")

    for task in done_tasks:
        print(
            f"\t {task.get('title')}"
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: python3 0-gather_data_from_an_API.py <employee_id>"
        )
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print(
            "Error: employee_id must be an integer"
        )
        sys.exit(1)

    get_employee_todos(emp_id)
