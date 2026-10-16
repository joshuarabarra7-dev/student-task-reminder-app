from task_service import TaskService


def show_menu():
    print("\n" + "=" * 40)
    print(" STUDENT TASK AND REMINDER APP")
    print("=" * 40)
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark task as completed")
    print("6. Add reminder")
    print("7. View reminders")
    print("8. Check upcoming/overdue tasks")
    print("0. Exit")


def main():
    service = TaskService()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            description = input("Description: ").strip()
            due_date = input("Due date (YYYY-MM-DD): ").strip()
            service.add_task(title, description, due_date)

        elif choice == "2":
            service.view_tasks()

        elif choice == "3":
            service.view_tasks()
            task_id = input("Enter task ID to update: ").strip()
            title = input("New title (leave blank to keep current): ").strip()
            description = input("New description (leave blank to keep current): ").strip()
            due_date = input("New due date YYYY-MM-DD (leave blank to keep current): ").strip()
            service.update_task(task_id, title, description, due_date)

        elif choice == "4":
            service.view_tasks()
            task_id = input("Enter task ID to delete: ").strip()
            service.delete_task(task_id)

        elif choice == "5":
            service.view_tasks()
            task_id = input("Enter task ID to mark completed: ").strip()
            service.complete_task(task_id)

        elif choice == "6":
            service.view_tasks()
            task_id = input("Enter the task ID for this reminder: ").strip()
            reminder_date = input("Reminder date and time (YYYY-MM-DD HH:MM): ").strip()
            service.add_reminder(task_id, reminder_date)

        elif choice == "7":
            service.view_reminders()

        elif choice == "8":
            service.check_due_tasks()

        elif choice == "0":
            print("Thank you for using Student Task and Reminder App!")
            break

        else:
            print("Invalid choice. Please select an option from the menu.")


if __name__ == "__main__":
    main()
