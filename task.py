class Task:
    """Represents one school task or activity."""

    def __init__(self, task_id, title, description, due_date, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["title"],
            data.get("description", ""),
            data.get("due_date", ""),
            data.get("status", "Pending"),
        )
