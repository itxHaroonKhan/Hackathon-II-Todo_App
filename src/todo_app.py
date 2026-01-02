"""
In-Memory Console Todo Application
A simple, in-memory Python console todo application that allows users to manage their tasks without any persistence.
"""

# Global task storage - list of dictionaries
tasks = []
next_task_id = 1


class Task:
    """
    Represents a single todo task with id, title, description, and completion status.
    """
    def __init__(self, task_id, title, description="", is_completed=False):
        """
        Initialize a new Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Required task title
            description (str, optional): Optional task description
            is_completed (bool): Completion status, defaults to False
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")

        if len(title) > 500:
            raise ValueError("Title must be 500 characters or less")

        if description and len(description) > 2000:
            raise ValueError("Description must be 2000 characters or less")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.is_completed = is_completed

    def to_dict(self):
        """
        Convert the Task instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed
        }

    def __str__(self):
        """
        String representation of the task for display purposes.

        Returns:
            str: Formatted string representation of the task
        """
        status = "[Done]" if self.is_completed else "[Pending]"
        result = f"[{self.id}] {self.title} - {status}"
        if self.description:
            result += f"\n    Description: {self.description}"
        return result


def add_task(title, description=""):
    """
    Add a new task to the in-memory task list.

    Args:
        title (str): Task title (required, non-empty)
        description (str, optional): Task description

    Returns:
        dict: The created task dictionary if successful, None if validation fails
    """
    global next_task_id

    try:
        # Validate title
        if not title or not title.strip():
            print("Error: Task title cannot be empty. Please enter a valid title.")
            return None

        if len(title) > 500:
            print("Error: Task title must be 500 characters or less.")
            return None

        if description and len(description) > 2000:
            print("Error: Task description must be 2000 characters or less.")
            return None

        # Create new task
        new_task = Task(next_task_id, title, description, False)

        # Add to global tasks list
        tasks.append(new_task.to_dict())

        # Increment next_task_id for the next task
        next_task_id += 1

        print(f"Task '{new_task.title}' added successfully with ID {new_task.id}.")
        return new_task.to_dict()

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error adding task: {e}")
        return None


def get_all_tasks():
    """
    Retrieve all tasks from the in-memory task list.

    Returns:
        list: List of all task dictionaries
    """
    return tasks


def get_task_by_id(task_id):
    """
    Retrieve a specific task by its ID.

    Args:
        task_id (int): Unique identifier of the task

    Returns:
        dict: Task dictionary if found, None if not found
    """
    try:
        # Validate that task_id is a positive integer
        if not isinstance(task_id, int) or task_id <= 0:
            return None

        # Find task with matching ID
        for task in tasks:
            if task["id"] == task_id:
                return task
        return None
    except Exception:
        return None


def update_task(task_id, title=None, description=None):
    """
    Update the title and/or description of an existing task.

    Args:
        task_id (int): Unique identifier of the task to update
        title (str, optional): New title for the task
        description (str, optional): New description for the task

    Returns:
        dict: Updated task dictionary if successful, None if validation fails
    """
    try:
        # Find the task to update
        task = get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return None

        # Prepare new values
        new_title = title if title is not None else task["title"]
        new_description = description if description is not None else task["description"]

        # Validate new title if provided
        if title is not None:
            if not title or not title.strip():
                print("Error: Task title cannot be empty. Please enter a valid title.")
                return None

            if len(title) > 500:
                print("Error: Task title must be 500 characters or less.")
                return None

        # Validate new description if provided
        if description is not None and description and len(description) > 2000:
            print("Error: Task description must be 2000 characters or less.")
            return None

        # Update the task in the global list
        for i, t in enumerate(tasks):
            if t["id"] == task_id:
                tasks[i] = {
                    "id": task_id,
                    "title": new_title.strip(),
                    "description": new_description.strip() if new_description else "",
                    "is_completed": task["is_completed"]
                }
                break

        print(f"Task with ID {task_id} updated successfully.")
        return tasks[i]

    except Exception as e:
        print(f"Unexpected error updating task: {e}")
        return None


def delete_task(task_id):
    """
    Remove a task from the in-memory task list.

    Args:
        task_id (int): Unique identifier of the task to delete

    Returns:
        bool: True if deletion successful, False if task not found
    """
    global tasks

    try:
        # Find the task to delete
        task = get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return False

        # Remove the task from the list
        tasks = [t for t in tasks if t["id"] != task_id]

        print(f"Task with ID {task_id} deleted successfully.")
        return True

    except Exception as e:
        print(f"Unexpected error deleting task: {e}")
        return False


def toggle_task_status(task_id):
    """
    Toggle the completion status of a task.

    Args:
        task_id (int): Unique identifier of the task to update

    Returns:
        dict: Updated task dictionary if successful, None if task not found
    """
    try:
        # Find the task to update
        task = get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return None

        # Toggle the completion status
        new_status = not task["is_completed"]

        # Update the task in the global list
        for i, t in enumerate(tasks):
            if t["id"] == task_id:
                tasks[i]["is_completed"] = new_status
                break

        status_text = "completed" if new_status else "incomplete"
        print(f"Task with ID {task_id} marked as {status_text}.")
        return tasks[i]

    except Exception as e:
        print(f"Unexpected error toggling task status: {e}")
        return None


def display_tasks():
    """
    Display all tasks in a readable CLI format.
    """
    all_tasks = get_all_tasks()

    if not all_tasks:
        print("\nNo tasks in your todo list.")
        return

    print("\nYour Todo List:")
    print("-" * 50)

    for task in all_tasks:
        status = "[Done]" if task["is_completed"] else "[Pending]"
        print(f"[{task['id']}] {task['title']} - {status}")
        if task["description"]:
            print(f"    Description: {task['description']}")
        print()


def display_menu():
    """
    Show the main menu options to the user.
    """
    print("\n" + "="*50)
    print("           TODO APPLICATION MENU")
    print("="*50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("-"*50)


def handle_user_input(choice):
    """
    Process user's menu selection and route to appropriate function.

    Args:
        choice (str): User's menu selection

    Returns:
        bool: True to continue running, False to exit
    """
    try:
        if choice == "1":
            # Add Task
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip()
            add_task(title, description)

        elif choice == "2":
            # View Tasks
            display_tasks()

        elif choice == "3":
            # Update Task
            try:
                task_id = int(input("Enter task ID to update: "))
            except ValueError:
                print("Error: Please enter a valid task ID (number).")
                return True

            print("Leave blank to keep current value.")
            new_title = input(f"Enter new title (current: {get_task_by_id(task_id)['title'] if get_task_by_id(task_id) else 'N/A'}): ").strip()
            new_description = input(f"Enter new description (current: {get_task_by_id(task_id)['description'] if get_task_by_id(task_id) else 'N/A'}): ").strip()

            # Only update if user provided new values
            update_kwargs = {}
            if new_title:
                update_kwargs["title"] = new_title
            if new_description:
                update_kwargs["description"] = new_description

            if update_kwargs:
                update_kwargs["task_id"] = task_id
                # Call update_task with the correct parameters
                update_task(task_id, **update_kwargs)
            else:
                print("No changes provided, task not updated.")

        elif choice == "4":
            # Delete Task
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Error: Please enter a valid task ID (number).")

        elif choice == "5":
            # Mark Task Complete/Incomplete
            try:
                task_id = int(input("Enter task ID to toggle status: "))
                toggle_task_status(task_id)
            except ValueError:
                print("Error: Please enter a valid task ID (number).")

        elif choice == "6":
            # Exit
            print("Thank you for using the Todo Application. Goodbye!")
            return False

        else:
            print("Invalid choice. Please enter a number between 1-6.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return True


def run_application():
    """
    Main application loop that displays menu and handles user interaction.
    """
    print("Welcome to the In-Memory Console Todo Application!")
    print("All data is stored in memory only and will be lost when the application exits.")

    while True:
        display_menu()
        choice = input("Please select an option (1-6): ").strip()

        if not handle_user_input(choice):
            break


# Only run the application if this file is executed directly
if __name__ == "__main__":
    run_application()