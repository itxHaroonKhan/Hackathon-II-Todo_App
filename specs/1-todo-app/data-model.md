# Data Model: In-Memory Python Console Todo Application

## Task Entity

### Fields
- **id** (integer, required, immutable)
  - Auto-generated unique identifier for the task
  - Sequential integer starting from 1
  - Used for all operations (update, delete, mark complete)

- **title** (string, required)
  - The main text/description of the task
  - Cannot be empty (validation required)
  - Maximum length: 500 characters (practical limit)

- **description** (string, optional)
  - Additional details about the task
  - Can be empty/None
  - Maximum length: 2000 characters (practical limit)

- **is_completed** (boolean, required)
  - Status indicator for task completion
  - Default value: False (incomplete)
  - Can be toggled between True/False

### Validation Rules
- `title` must not be empty or contain only whitespace
- `id` must be unique within the task list
- `id` must be a positive integer
- `title` length should be 1-500 characters
- `description` length should be 0-2000 characters
- `is_completed` must be boolean value

### State Transitions
- `is_completed` can transition from False → True (mark complete)
- `is_completed` can transition from True → False (mark incomplete)
- All other fields remain constant except during update operations

## Task List Collection

### Structure
- In-memory storage using Python list data structure
- Each element is a Task entity (dictionary with fields above)
- Maintains insertion order (FIFO)

### Operations
- Add: Append new Task to the end of the list
- Read: Iterate through list to display all tasks
- Update: Find by id, modify specific fields
- Delete: Remove by id, maintain list integrity
- Search: Find by id for operations

### Constraints
- No duplicate IDs allowed
- IDs must remain consistent after operations
- List must handle empty state gracefully