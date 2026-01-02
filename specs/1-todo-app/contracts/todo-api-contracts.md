# API Contracts: In-Memory Python Console Todo Application

## Task Management Functions

### `add_task(title, description=None)`
**Purpose**: Add a new task to the in-memory task list

**Input**:
- `title` (string, required): Task title (1-500 characters, not empty)
- `description` (string, optional): Task description (0-2000 characters)

**Output**:
- Success: Returns task dictionary with id, title, description, and is_completed
- Error: Returns None with error message displayed to user

**Side Effects**: Appends new task to global task list

**Validation**:
- Title must not be empty or contain only whitespace
- Title length must be 1-500 characters
- Description length must be 0-2000 characters

---

### `get_all_tasks()`
**Purpose**: Retrieve all tasks from the in-memory task list

**Input**: None

**Output**:
- Returns list of task dictionaries
- Returns empty list if no tasks exist

**Side Effects**: None

---

### `get_task_by_id(task_id)`
**Purpose**: Retrieve a specific task by its ID

**Input**:
- `task_id` (integer): Unique identifier of the task

**Output**:
- Success: Returns task dictionary if found
- Error: Returns None if task doesn't exist

**Validation**:
- task_id must be a positive integer
- task_id must exist in the task list

---

### `update_task(task_id, title=None, description=None)`
**Purpose**: Update the title and/or description of an existing task

**Input**:
- `task_id` (integer): Unique identifier of the task to update
- `title` (string, optional): New title for the task
- `description` (string, optional): New description for the task

**Output**:
- Success: Returns updated task dictionary
- Error: Returns None with error message displayed to user

**Validation**:
- task_id must exist in the task list
- If title is provided, it must not be empty
- Title length must be 1-500 characters if provided
- Description length must be 0-2000 characters if provided

---

### `delete_task(task_id)`
**Purpose**: Remove a task from the in-memory task list

**Input**:
- `task_id` (integer): Unique identifier of the task to delete

**Output**:
- Success: Returns True if deletion successful
- Error: Returns False with error message displayed to user

**Validation**:
- task_id must exist in the task list

---

### `toggle_task_status(task_id)`
**Purpose**: Toggle the completion status of a task

**Input**:
- `task_id` (integer): Unique identifier of the task to update

**Output**:
- Success: Returns updated task dictionary
- Error: Returns None with error message displayed to user

**Validation**:
- task_id must exist in the task list

---

## CLI Interface Functions

### `display_menu()`
**Purpose**: Show the main menu options to the user

**Input**: None
**Output**: Prints menu to console
**Side Effects**: None

---

### `handle_user_input(choice)`
**Purpose**: Process user's menu selection and route to appropriate function

**Input**:
- `choice` (string): User's menu selection

**Output**: Executes appropriate task management function
**Side Effects**: May modify task list or display information to user

---

### `run_application()`
**Purpose**: Main application loop that displays menu and handles user interaction

**Input**: None
**Output**: Continuous menu interaction until user chooses to exit
**Side Effects**: Maintains in-memory task list throughout execution