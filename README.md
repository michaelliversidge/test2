# Todo CLI

A simple command-line to-do list manager built in Python.

## Features

- Add tasks
- List all tasks
- Mark tasks as complete
- Delete tasks
- Persistent storage (JSON file)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Add a task
python todo.py add "Buy groceries"

# List all tasks
python todo.py list

# Mark a task as complete (by ID)
python todo.py done 1

# Delete a task (by ID)
python todo.py delete 1

# Clear all tasks
python todo.py clear
```

## Commands

- `add <description>` - Add a new task
- `list` - Show all tasks
- `done <id>` - Mark a task as complete
- `delete <id>` - Delete a task
- `clear` - Delete all tasks

## Task Storage

Tasks are stored in `tasks.json` in the current directory.
