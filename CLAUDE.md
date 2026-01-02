# Claude Code Usage Instructions

This project was developed using Claude Code and Spec-Kit Plus following a spec-driven development approach.

## Project Structure

```
PROJECT_ROOT/
├── src/
│   └── todo_app.py              # Main application file
├── specs/
│   └── 1-todo-app/
│       ├── spec.md              # Feature specification
│       ├── plan.md              # Implementation plan
│       ├── tasks.md             # Task breakdown
│       ├── checklists/          # Quality checklists
│       └── other design docs/
├── test_todo_app.py             # Test script for functions
├── README.md                    # Project documentation
├── CLAUDE.md                    # Claude Code usage instructions
└── other project files
```

## Spec-Driven Development Workflow

This project follows the Spec-Kit Plus methodology:

1. **Specification** (`spec.md`): Defines user stories, requirements, and acceptance criteria
2. **Planning** (`plan.md`): Technical architecture and implementation approach
3. **Task Breakdown** (`tasks.md`): Granular implementation tasks
4. **Implementation**: Code development following the task list

## Running the Application

To run the todo application:

```bash
python src/todo_app.py
```

## Running Tests

To verify the functionality:

```bash
python test_todo_app.py
```

## Claude Code Commands Used

- `/sp.specify`: Create/update feature specification
- `/sp.plan`: Generate implementation plan
- `/sp.tasks`: Break down implementation into tasks
- `/sp.implement`: Execute the implementation following tasks
- `/sp.adr`: Create architecture decision records
- `/sp.phr`: Create prompt history records

## Development Approach

The todo application was implemented following these principles:
- Single-file Python application for simplicity
- In-memory storage only (no persistence)
- Console-based CLI interface
- Clean code with proper validation
- Error handling for all user inputs
- PEP8 compliant code