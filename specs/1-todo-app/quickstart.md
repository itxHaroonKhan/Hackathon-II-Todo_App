# Quickstart Guide: In-Memory Python Console Todo Application

## Prerequisites
- Python 3.13 or higher
- Console/terminal access
- No external packages required

## Setup
1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory containing `todo_app.py`
3. Run the application using Python:

```bash
python todo_app.py
```

## Basic Usage
1. The application starts with a menu showing available options
2. Enter the number corresponding to your desired action
3. Follow the prompts to provide required information
4. The application will confirm successful operations or display error messages

## Available Features
- **Add Task**: Create a new todo item with title and optional description
- **View Tasks**: Display all tasks with their ID, title, and completion status
- **Update Task**: Modify the title or description of an existing task
- **Delete Task**: Remove a task by its ID
- **Mark Complete/Incomplete**: Toggle the completion status of a task
- **Exit**: Quit the application (data will be lost as it's in-memory only)

## Example Workflow
1. Start the application: `python todo_app.py`
2. Select "Add Task" and enter a title like "Buy groceries"
3. Optionally add a description like "Milk, bread, eggs"
4. Select "View Tasks" to see your task list
5. Select "Mark Complete" and enter the task ID to mark it complete
6. Select "Exit" when finished

## Error Handling
- Invalid inputs will show clear error messages
- Non-existent task IDs will be rejected with explanation
- Empty titles will be rejected with prompt to enter valid title
- The application will never crash due to invalid user input