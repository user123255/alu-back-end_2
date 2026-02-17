#!/usr/bin/python3
"""
Export all tasks for a given employee ID to a CSV file.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
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

    # Prepare CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
