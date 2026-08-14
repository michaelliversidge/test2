import pytest
import json
import os
from pathlib import Path
from todo import load_tasks, save_tasks, add_task, mark_done, delete_task


@pytest.fixture
def cleanup_tasks():
    """Clean up test tasks file after each test."""
    yield
    if Path("tasks.json").exists():
        os.remove("tasks.json")


def test_add_task(cleanup_tasks, capsys):
    """Test adding a new task."""
    add_task("Test task")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test task"
    assert tasks[0]["completed"] is False


def test_list_tasks_empty(cleanup_tasks, capsys):
    """Test listing tasks when empty."""
    from todo import list_tasks
    list_tasks()
    captured = capsys.readouterr()
    assert "No tasks yet!" in captured.out


def test_mark_done(cleanup_tasks):
    """Test marking a task as complete."""
    add_task("Task to complete")
    mark_done(1)
    tasks = load_tasks()
    assert tasks[0]["completed"] is True


def test_delete_task(cleanup_tasks):
    """Test deleting a task."""
    add_task("Task to delete")
    delete_task(1)
    tasks = load_tasks()
    assert len(tasks) == 0


def test_multiple_tasks(cleanup_tasks):
    """Test handling multiple tasks."""
    add_task("First task")
    add_task("Second task")
    add_task("Third task")
    tasks = load_tasks()
    assert len(tasks) == 3
    assert tasks[0]["id"] == 1
    assert tasks[1]["id"] == 2
    assert tasks[2]["id"] == 3


def test_task_persistence(cleanup_tasks):
    """Test that tasks persist across loads."""
    add_task("Persistent task")
    tasks1 = load_tasks()
    tasks2 = load_tasks()
    assert tasks1 == tasks2
