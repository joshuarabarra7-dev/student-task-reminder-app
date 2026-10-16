import json
from datetime import datetime
from pathlib import Path

from task import Task
from reminder import Reminder


class TaskService:
    """Handles task and reminder operations and saves data in a JSON file."""

    def __init__(self, data_file="tasks.json"):
        # Store the JSON file in the same folder as this Python file.
        self.data_file = Path(__file__).resolve().parent / data_file
        self.tasks = []
        self.reminders = []
        self.load_data()

    def load_data(self):
        if not self.data_file.exists():
            self.save_data()
            return

        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
            self.tasks = [Task.from_dict(item) for item in data.get("tasks", [])]
            self.reminders = [
                Reminder.from_dict(item) for item in data.get("reminders", [])
            ]
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            print(f"Could not read saved data: {error}")
            print("Starting with an empty task list. Check tasks.json if needed.")
            self.tasks = []
            self.reminders = []

    def save_data(self):
        data = {
            "tasks": [task.to_dict() for task in self.tasks],
            "reminders": [reminder.to_dict() for reminder in self.reminders],
        }
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def _next_task_id(self):
        return max((task.task_id for task in self.tasks), default=0) + 1

    def _next_reminder_id(self):
        return max((reminder.reminder_id for reminder in self.reminders), default=0) + 1

    @staticmethod
    def _valid_date(value, date_format):
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            return False

    def add_task(self, title, description, due_date):
        if not title:
            print("Task title cannot be empty.")
            return
        if not self._valid_date(due_date, "%Y-%m-%d"):
            print("Invalid date. Please use YYYY-MM-DD, for example 2026-10-20.")
            return

        task = Task(self._next_task_id(), title, description, due_date)
        self.tasks.append(task)
        self.save_data()
        print(f"Task added successfully. Task ID: {task.task_id}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet. Add a task first.")
            return

        print("\n--- TASK LIST ---")
        for task in self.tasks:
            print(f"ID: {task.task_id} | {task.title}")
            print(f"  Description: {task.description or 'None'}")
            print(f"  Due date: {task.due_date} | Status: {task.status}")

    def update_task(self, task_id, title="", description="", due_date=""):
        task = self._find_task(task_id)
        if task is None:
            print("Task not found.")
            return

        if due_date and not self._valid_date(due_date, "%Y-%m-%d"):
            print("Invalid date. Please use YYYY-MM-DD.")
            return

        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date

        self.save_data()
        print("Task updated successfully.")

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            print("Task not found.")
            return

        self.tasks.remove(task)
        # Also remove reminders connected to the deleted task.
        self.reminders = [
            reminder for reminder in self.reminders if reminder.task_id != task.task_id
        ]
        self.save_data()
        print("Task and its reminders deleted successfully.")

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            print("Task not found.")
            return

        task.status = "Completed"
        self.save_data()
        print("Task marked as completed.")

    def add_reminder(self, task_id, reminder_time):
        task = self._find_task(task_id)
        if task is None:
            print("Task not found. Please enter an existing task ID.")
            return
        if not self._valid_date(reminder_time, "%Y-%m-%d %H:%M"):
            print("Invalid date/time. Use YYYY-MM-DD HH:MM, e.g. 2026-10-20 08:30.")
            return

        reminder = Reminder(self._next_reminder_id(), task.task_id, reminder_time)
        self.reminders.append(reminder)
        self.save_data()
        print(f"Reminder saved for task: {task.title}")

    def view_reminders(self):
        if not self.reminders:
            print("No reminders yet.")
            return

        print("\n--- REMINDERS ---")
        for reminder in self.reminders:
            task = self._find_task(str(reminder.task_id))
            task_title = task.title if task else "Task no longer available"
            print(
                f"Reminder ID: {reminder.reminder_id} | Task: {task_title} "
                f"| Reminder time: {reminder.reminder_time}"
            )

    def check_due_tasks(self):
        now = datetime.now()
        found = False
        print("\n--- UPCOMING / OVERDUE TASKS ---")
        for task in self.tasks:
            if task.status == "Completed":
                continue
            due = datetime.strptime(task.due_date, "%Y-%m-%d")
            days_left = (due.date() - now.date()).days
            if days_left < 0:
                label = f"OVERDUE by {abs(days_left)} day(s)"
            elif days_left == 0:
                label = "DUE TODAY"
            elif days_left <= 3:
                label = f"Due in {days_left} day(s)"
            else:
                continue
            print(f"ID: {task.task_id} | {task.title} | {label} | Due: {task.due_date}")
            found = True

        if not found:
            print("No tasks due today, overdue, or due within the next 3 days.")

        # Show reminders whose scheduled time has arrived.
        due_reminders = []
        for reminder in self.reminders:
            reminder_dt = datetime.strptime(reminder.reminder_time, "%Y-%m-%d %H:%M")
            if reminder_dt <= now:
                task = self._find_task(str(reminder.task_id))
                if task and task.status != "Completed":
                    due_reminders.append((reminder, task))

        if due_reminders:
            print("\n--- REMINDERS THAT ARE DUE ---")
            for reminder, task in due_reminders:
                print(f"Reminder for '{task.title}' was scheduled at {reminder.reminder_time}.")
            print("These are console reminders; this program does not send phone/desktop notifications.")

    def _find_task(self, task_id):
        try:
            task_id = int(task_id)
        except (TypeError, ValueError):
            return None
        return next((task for task in self.tasks if task.task_id == task_id), None)
