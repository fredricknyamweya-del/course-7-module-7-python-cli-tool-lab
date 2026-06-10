class Task:
    def __init__(self, name: str):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True


class User:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)
