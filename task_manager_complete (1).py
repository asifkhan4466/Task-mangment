
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = completed

    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.title} | {self.description} | Due: {self.due_date.date()} | {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        self.tasks.append(Task(title, description, due_date))

    def list_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx+1}. {task}")

    def edit_task(self, index, title=None, description=None, due_date=None):
        task = self.tasks[index]
        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = datetime.strptime(due_date, "%Y-%m-%d")

    def delete_task(self, index):
        del self.tasks[index]

    def mark_complete(self, index):
        self.tasks[index].completed = True

    def mark_incomplete(self, index):
        self.tasks[index].completed = False

    def filter_by_status(self, status=True):
        return [task for task in self.tasks if task.completed == status]


def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Mark Task as Incomplete")
    print("7. View Completed Tasks")
    print("8. View Incomplete Tasks")
    print("9. Exit")


def main():
    tm = TaskManager()
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            tm.add_task(title, desc, due)

        elif choice == "2":
            tm.list_tasks()

        elif choice == "3":
            idx = int(input("Task number to edit: ")) - 1
            title = input("New title (leave blank to skip): ")
            desc = input("New description: ")
            due = input("New due date (YYYY-MM-DD) : ")
            tm.edit_task(idx, title or None, desc or None, due or None)

        elif choice == "4":
            idx = int(input("Task number to delete: ")) - 1
            tm.delete_task(idx)

        elif choice == "5":
            idx = int(input("Task number to mark complete: ")) - 1
            tm.mark_complete(idx)

        elif choice == "6":
            idx = int(input("Task number to mark incomplete: ")) - 1
            tm.mark_incomplete(idx)

        elif choice == "7":
            tasks = tm.filter_by_status(True)
            for t in tasks:
                print(t)

        elif choice == "8":
            tasks = tm.filter_by_status(False)
            for t in tasks:
                print(t)

        elif choice == "9":
            break


# Unit tests
import unittest

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()
        self.tm.add_task("Test Task", "Test Description", "2025-06-01")

    def test_add_task(self):
        self.assertEqual(len(self.tm.tasks), 1)

    def test_edit_task(self):
        self.tm.edit_task(0, title="New Title")
        self.assertEqual(self.tm.tasks[0].title, "New Title")

    def test_mark_complete(self):
        self.tm.mark_complete(0)
        self.assertTrue(self.tm.tasks[0].completed)


if __name__ == "__main__":
    main()
