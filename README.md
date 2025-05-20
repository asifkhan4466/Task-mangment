# Console-Based Task Management System

This is a simple Python-based task management system designed for the command line.
It allows users to create, update, delete, and filter tasks based on their status.

## Features

- Add new tasks with title, description, and due date
- View all tasks in a list format
- Edit task details
- Delete tasks
- Mark tasks as complete or incomplete
- Filter tasks by completion status (complete/incomplete)
- Includes unit tests for task management logic
- (Optional) File-based persistent storage (storage.py)
- (Optional) Utilities for date validation (utils.py)

## Project Structure

```
task_manager_project/
â”‚
â”œâ”€â”€ main.py                  # Entry point CLI application
â”œâ”€â”€ task.py                  # Task class definition
â”œâ”€â”€ task_manager.py          # Business logic
â”œâ”€â”€ storage.py               # Optional: File I/O for saving/loading tasks
â”œâ”€â”€ utils.py                 # Optional: Helper utilities like date validation
â”œâ”€â”€ test_task_manager.py     # Unit tests using unittest module
â”œâ”€â”€ README.md                # Project documentation
â””â”€â”€ requirements.txt         # Python dependencies
```

## Requirements

- Python 3.10 or above

## How to Run

1. Clone the repository or download the ZIP.
2. Navigate to the project directory in your terminal.
3. Run the application:

```bash
python main.py
```

## How to Run Tests

```bash
python -m unittest test_task_manager.py
```

## Optional Enhancements

- Add a GUI using Tkinter or PyQt
- Integrate with a SQLite or JSON file for persistent storage
- Add deadlines and automatic reminders

## Author

Created as part of a Software Construction and Development Assignment.
