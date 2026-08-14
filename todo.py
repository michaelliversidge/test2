#!/usr/bin/env python3
"""
Simple command-line to-do list manager.
"""

import json
import sys
from pathlib import Path
from datetime import datetime


TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if Path(TASKS_FILE).exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Added: {description}")


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\nTasks:")
    print("-" * 50)
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['id']:2d}. {task['description']}")
    print("-" * 50)
    print(f"Total: {len(tasks)} | Completed: {sum(1 for t in tasks if t['completed'])}")


def mark_done(task_id):
    """Mark a task as complete."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"✓ Marked complete: {task['description']}")
            return
    print(f"✗ Task {task_id} not found")


def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(i)
            save_tasks(tasks)
            print(f"✓ Deleted: {deleted['description']}")
            return
    print(f"✗ Task {task_id} not found")


def clear_all():
    """Delete all tasks."""
    response = input("Are you sure? This cannot be undone. (yes/no): ")
    if response.lower() == "yes":
        save_tasks([])
        print("✓ All tasks cleared")
    else:
        print("Cancelled")


def show_help():
    """Show help message."""
    print("""
Todo CLI - Simple task manager

Usage:
  python todo.py add "<description>"    Add a new task
  python todo.py list                   List all tasks
  python todo.py done <id>              Mark task as complete
  python todo.py delete <id>            Delete a task
  python todo.py clear                  Clear all tasks
  python todo.py help                   Show this help message
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    if command == "add" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) > 2:
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("✗ Invalid task ID")
    elif command == "delete" and len(sys.argv) > 2:
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("✗ Invalid task ID")
    elif command == "clear":
        clear_all()
    elif command == "help":
        show_help()
    else:
        print(f"✗ Unknown command: {command}")
        show_help()


if __name__ == "__main__":
    main()
