class Reminder:
    """Represents a reminder connected to a task."""

    def __init__(self, reminder_id, task_id, reminder_time):
        self.reminder_id = reminder_id
        self.task_id = task_id
        self.reminder_time = reminder_time

    def to_dict(self):
        return {
            "reminder_id": self.reminder_id,
            "task_id": self.task_id,
            "reminder_time": self.reminder_time,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["reminder_id"], data["task_id"], data["reminder_time"])
