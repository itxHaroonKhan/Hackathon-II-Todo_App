# Data Model: Phase II — Full-Stack Web Todo Application

## Entity: Task

### Fields
- `id` (Integer, Primary Key, Auto-increment)
  - Type: Integer
  - Constraints: Primary Key, Auto-increment
  - Description: Unique identifier for each task

- `title` (String, Required)
  - Type: String(255)
  - Constraints: Not Null, Length 1-255
  - Description: Required title of the task

- `description` (String, Optional)
  - Type: String(1000)
  - Constraints: Nullable
  - Description: Optional detailed description of the task

- `is_completed` (Boolean)
  - Type: Boolean
  - Constraints: Not Null, Default False
  - Description: Completion status of the task

- `created_at` (DateTime)
  - Type: DateTime
  - Constraints: Not Null, Default current timestamp
  - Description: Timestamp when the task was created

### Validation Rules
- Title must be 1-255 characters
- Description must be 0-1000 characters
- `is_completed` defaults to False when creating a new task
- `created_at` is automatically set to current time when creating a task

### State Transitions
- New task: `is_completed` = False
- Completed task: `is_completed` = True
- Reopened task: `is_completed` = False

## Database Schema

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Indexes
- Primary key index on `id` (automatic)
- Consider adding index on `is_completed` if filtering by completion status is common

## Relationships
- The Task entity is standalone with no relationships to other entities in Phase II
- Future phases may introduce user relationships for multi-user support

## SQLModel Implementation

```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TaskCreate(TaskBase):
    title: str

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TaskRead(TaskBase):
    id: int
    created_at: datetime
```