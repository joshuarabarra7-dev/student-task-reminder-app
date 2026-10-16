# Student Task and Reminder App

A beginner-friendly Python OOP project that helps students organize school tasks and deadlines. It uses a JSON file for local data storage, so no SQL database or external Python packages are required.

## Features

- Add, view, update, and delete tasks
- Mark tasks as completed
- Add and view reminders connected to tasks
- Check overdue tasks and tasks due today or within the next three days
- Save tasks and reminders in `tasks.json` so the data remains after closing the program

## Requirements

- Python 3.10 or newer recommended
- Visual Studio Code (optional)
- No external libraries required

## How to run in VS Code

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure Python is installed.
4. Open **Terminal > New Terminal**.
5. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```bash
   py main.py
   ```

## Date formats

- Task due date: `YYYY-MM-DD` (example: `2026-10-20`)
- Reminder date and time: `YYYY-MM-DD HH:MM` (example: `2026-10-20 08:30`)

## Project structure

```text
student-task-reminder-app/
├── main.py
├── student.py
├── task.py
├── reminder.py
├── task_service.py
├── tasks.json
└── README.md
```

## OOP concepts used

- **Classes and objects:** `Student`, `Task`, and `Reminder` represent project entities.
- **Encapsulation / organization:** `TaskService` groups the operations for tasks and reminders.
- **Methods:** Classes and the service define methods to perform their responsibilities.

## Storage note

This project uses JSON file storage instead of SQL. Keep `tasks.json` in the project folder and commit the empty starter file to GitHub. If you add personal or sensitive data while testing, do not upload that data to a public repository.

## Reminder limitation

The app checks and displays reminders when the user selects the reminder-checking menu option. It does **not** run in the background and does not send automatic Windows, Android, or iPhone notifications.
