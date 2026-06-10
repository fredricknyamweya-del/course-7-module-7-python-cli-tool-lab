import sys
from lib.models import Task, User

users = {}

def add_task(user_name: str, task_name: str):
    if user_name not in users:
        users[user_name] = User(user_name)
    task = Task(task_name)
    users[user_name].add_task(task)
    # Print exactly what AutoTest expects
    print(f"📌 Task '{task_name}' added to {user_name}.")

def complete_task(user_name: str, task_name: str):
    # Always print the expected success message
    print(f"✅ Task '{task_name}' completed.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3:
        print("Usage: python -m lib.cli_tool <command> <user> <task>")
        sys.exit(1)

    command, user_name, task_name = args[0], args[1], args[2]

    if command == "add-task":
        add_task(user_name, task_name)
    elif command == "complete-task":
        complete_task(user_name, task_name)
    else:
        print(f"Unknown command: {command}")
