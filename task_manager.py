from typing import Any, TypedDict

class Task(TypedDict):
    title: str
    completed: bool


def add_task(title: str) -> str:
    tasks.append({'title': title, 'completed': False})
    return f"Task {title} added successfully"


def list_tasks() -> list[Task]:
    return tasks


def complete_task(task_number: int) -> str:
    if task_number < 1 or task_number > len(tasks):
        return "Invalid task number"
    task = tasks[task_number - 1]
    task['completed'] = True
    return "Task completed successfully"


def remove_task(task_number: int) -> str:
    if task_number < 1 or task_number > len(tasks):
        return "Invalid task number"

    tasks.pop(task_number - 1)
    return "Task removed successfully"


tasks: list[Task] = []


if __name__ == "__main__":
    print("Testing...")
    print(add_task("Learn Python"))
    print(add_task("Learn Google ADK"))
    print(complete_task(2))

    print(list_tasks())
    print(remove_task(2))

    print(list_tasks())
