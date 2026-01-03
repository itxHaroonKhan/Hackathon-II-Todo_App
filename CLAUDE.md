# Claude Code Usage Instructions

This project was developed using Claude Code and Spec-Kit Plus following a spec-driven development approach.

## Project Structure

```
PROJECT_ROOT/
├── backend/                 # FastAPI backend application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── database/
│   │   └── api/
│   ├── requirements.txt
│   └── .env
├── frontend/                # Next.js frontend application
│   ├── package.json
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── services/
│   └── .env
├── specs/                   # Specification files
│   └── 001-fullstack-web-todo/
│       ├── spec.md          # Feature specification
│       ├── plan.md          # Implementation plan
│       ├── tasks.md         # Task breakdown
│       ├── checklists/      # Quality checklists
│       └── other design docs/
├── specs_history/           # Historical specs
├── README.md                # Project documentation
├── CLAUDE.md                # Claude Code usage instructions
└── other project files
```

## Spec-Driven Development Workflow

This project follows the Spec-Kit Plus methodology:

1. **Specification** (`spec.md`): Defines user stories, requirements, and acceptance criteria
2. **Planning** (`plan.md`): Technical architecture and implementation approach
3. **Task Breakdown** (`tasks.md`): Granular implementation tasks
4. **Implementation**: Code development following the task list

## Claude Code Commands Used

- `/sp.specify`: Create/update feature specification
- `/sp.plan`: Generate implementation plan
- `/sp.tasks`: Break down implementation into tasks
- `/sp.implement`: Execute the implementation following tasks
- `/sp.adr`: Create architecture decision records
- `/sp.phr`: Create prompt history records

## Development Approach

The todo application was implemented following these principles:
- Backend-first development approach
- API-first architecture with clean separation of concerns
- FastAPI backend with SQLModel ORM
- Next.js frontend consuming backend APIs only
- Neon PostgreSQL for persistent data storage
- PEP8 compliant code with proper validation
- Error handling for all user inputs