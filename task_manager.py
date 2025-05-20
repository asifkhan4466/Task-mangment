from task import Task

class TaskManager:
    def _init_(self):
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
            task.due_date = due_date

    def delete_task(self, index):
        del self.tasks[index]

    def mark_complete(self, index):
        self.tasks[index].completed = True

    def mark_incomplete(self, index):
        self.tasks[index].completed = False

    def filter_by_status(self, status=True):
        return [task for task in self.tasks if task.completed == status]
