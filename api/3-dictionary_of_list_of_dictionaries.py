#!/usr/bin/python3
"""
Export all employees' TODO tasks to a JSON file.
Format:
{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        ...
    ],
    ...
}
"""

import json
import requests


if __name__ == "__main__":
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch all todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare dictionary
    all_employees_tasks = {}

    for user in users_data:
        user_id = str(user.get("id"))
        username = user.get("name")

        # List to hold this user's tasks
        user_tasks = []

        for task in todos_data:
            if task.get("userId") == user.get("id"):
                task_dict = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_dict)

        all_employees_tasks[user_id] = user_tasks

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file)
