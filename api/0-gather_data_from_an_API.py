#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID.

Requirements:
- Uses requests module
- Accepts employee ID as a parameter
- Displays progress in the format:
  Employee EMPLOYEE_NAME is done with tasks(
      NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
      TASK_TITLE
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Base API URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct endpoints
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user and todos
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Check for request success
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data from API.")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    # Print summary
    print(
        f"Employee {employee_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
    )

    # Print completed task titles
    for task in done_tasks:
        print(f"\t{task.get('title')}")
