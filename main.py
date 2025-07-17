import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file, return empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: Could not decode tasks file. Starting with an empty list.")
        return []

def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error: Unable to save tasks. {e}")

def add_task(tasks):
    """Prompt the user to enter a task and append it to the list as Pending."""
    task_description = input("Enter the new task: ").strip()
    if not task_description:
        print("Task description cannot be empty.")
        return
    tasks.append({"description": task_description, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully.\n")

def list_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks in your Todo list.\n")
        return
    print("Todo List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['description']} [{task['status']}]")
    print()

def complete_task(tasks):
    """Prompt the user for a task number and mark the task as completed."""
    if not tasks:
        print("No tasks to complete.\n")
        return
    try:
        task_num = int(input("Enter the task number to complete: "))
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1]['status'] == "Done":
                print("Task is already marked as completed.\n")
                return
            tasks[task_num - 1]['status'] = "Done"
            save_tasks(tasks)
            print(f"Task #{task_num} marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def remove_task(tasks):
    """Prompt the user for a task number and remove it from the list."""
    if not tasks:
        print("No tasks to remove.\n")
        return
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed['description']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main_menu():
    """Present the menu and process user choices."""
    tasks = load_tasks()
    menu_options = {
        "1": add_task,
        "2": list_tasks,
        "3": complete_task,
        "4": remove_task,
        "5": exit_application
    }

    while True:
        print("=== Todo Application ===")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Complete a task")
        print("4. Remove a task")
        print("5. Exit")
        choice = input("Select an option: ").strip()

        action = menu_options.get(choice)
        if action:
            action(tasks)
        else:
            print("Invalid selection, please try again.\n")

def exit_application(tasks=None):
    """Exit the application gracefully."""
    print("Exiting application. Goodbye!")
    exit()

if __name__ == "__main__":
    main_menu()
