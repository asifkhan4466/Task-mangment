from datetime import datetime

class Task:
    def _init_(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = completed

    def _str_(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.title} | {self.description} | Due: {self.due_date.date()} | {status}"