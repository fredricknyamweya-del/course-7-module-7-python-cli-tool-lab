import sys
from lib.models import Task, User

users = {}

def add_task(user_name: str, task_name: str):
    if user_name not in users:
        users[user_name] = User(user_name)
    task = Task(task_name)
    users[user_name].add_task(task)
    print(f"📌 Task '{task_name}' added to {user_name}.")

def complete_task(user_name: str, task_name: str):
    if user_name in users:
        for task in users[user_name].tasks:
            if task.name == task_name:
                task.complete()
                print(f"✅ Task '{task_name}' completed.")
                return
    print(f"⚠️ Task '{task_name}' not found for {user_name}.")

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
