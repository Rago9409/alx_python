"""fetching employee,TODO lists and counting completed tasks
"""

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {employee['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

    # Export data to CSV
    with open(f"{employee_id}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, employee['username'], todo['completed'], todo['title']])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)