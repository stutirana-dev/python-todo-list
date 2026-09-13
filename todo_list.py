tasks = []


def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks found.\n")
        return

    print("\n--- Your Tasks ---")

    for number, item in enumerate(tasks, start=1):
        status = "✓" if item["completed"] else "✗"
        print(f"{number}. [{status}] {item['task']}")

    print()


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            print(f"Deleted: {deleted['task']}\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("=== Python To-Do List ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


main()