from task_manager import add_task, tasks, complete_task, remove_task, list_tasks


def test_add_task():
    tasks.clear()
    add_task("Learn Python")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Learn Python"
    assert tasks[0]["completed"] is False


def test_complete_task():
    tasks.clear()
    add_task("Learn Docker")
    complete_task(1)
    assert tasks[0]["completed"] is True


def test_complete_task_invalid_number():
    tasks.clear()
    add_task("Learn Kubernetes")
    result = complete_task(999)
    assert result == "Invalid task number"
    assert tasks[0]["completed"] is False


def test_remove_task():
    tasks.clear()
    add_task("Learn Python")
    add_task("Learn Docker")
    remove_task(1)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Learn Docker"


def test_remove_task_invalid_number():
    tasks.clear()
    add_task("Learn Docker")
    result = remove_task(999)
    assert result == "Invalid task number"
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Learn Docker"


def test_list_tasks():
    tasks.clear()
    add_task("Learn Python")
    add_task("Learn Docker")
    result = list_tasks()
    assert len(result) == 2
    assert result[0]["title"] == "Learn Python"
    assert result[1]["title"] == "Learn Docker"
