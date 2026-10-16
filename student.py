class Student:
    """Represents a student using the application."""

    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
