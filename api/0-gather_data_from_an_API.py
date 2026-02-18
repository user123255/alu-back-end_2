import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    base_url = (
        "https://jsonplaceholder.typicode.com"
    )

    user_url = "{}/users/{}".format(
        base_url,
        employee_id
    )

    todos_url = "{}/users/{}/todos".format(
        base_url,
        employee_id
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
        "Employee {} is done with tasks ({}/{}):".format(
            employee_name,
            number_done_tasks,
            total_tasks
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
