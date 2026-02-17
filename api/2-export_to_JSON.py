#!/usr/bin/python3
"""
Export all tasks for a given employee ID to a JSON file.
Format:
{
    "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        ...
    ]
}
"""

import json
import sys
import requests


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # URLs for fetching user and todos data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("name")

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare JSON structure
    tasks_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    json_data = {employee_id: tasks_list}

    # Write to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file)
