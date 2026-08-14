# Todo CLI Project

This is a simple command-line to-do list manager built in Python. It's designed as a testing ground for exploring how Copilot can help with software development tasks.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/michaelliversidge/test2.git
cd test2

# Run the app
python todo.py add "Buy groceries"
python todo.py list
python todo.py done 1
```

## What's Included

- **todo.py** - Main application with all core features
- **test_todo.py** - Unit tests using pytest
- **requirements.txt** - Project dependencies
- **README.md** - Documentation

## Features

✓ Add tasks  
✓ List all tasks with completion status  
✓ Mark tasks as complete  
✓ Delete individual tasks  
✓ Clear all tasks  
✓ Persistent storage (JSON)  
✓ Task timestamps  
✓ Full test coverage  

## Commands

```bash
python todo.py add "Buy milk"           # Add a task
python todo.py list                     # Show all tasks
python todo.py done 1                   # Mark task 1 as complete
python todo.py delete 1                 # Delete task 1
python todo.py clear                    # Delete all tasks
python todo.py help                     # Show help
```

## Running Tests

```bash
pip install -r requirements.txt
pytest test_todo.py -v
```

## Next Steps

Ideas for extending this project:
- Add due dates and reminders
- Implement task categories/tags
- Add priority levels
- Create a web UI with Flask
- Add data export (CSV, PDF)
- Implement recurring tasks
- Add search/filter functionality
