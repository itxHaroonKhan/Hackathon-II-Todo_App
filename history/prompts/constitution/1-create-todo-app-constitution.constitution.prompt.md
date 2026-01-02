---
id: 1
title: Create Todo App Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Claude Code
command: /sp.constitution
labels: [constitution, todo-app, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
/sp.constitution

Project: In-Memory Console-Based Todo Application (Phase I)

Objective:
Build a clean, reliable, in-memory Python console Todo app that strictly follows software engineering fundamentals before any database, UI, or AI integration.

Tech Stack:
- Language: Python 3.x
- Runtime: Console / CLI
- Storage: In-memory only (no files, no DB, no external services)
- Tools: Claude Code, Spec-Kit compatible

Core Principles:
- Simplicity over cleverness (no over-engineering)
- Deterministic behavior (same input → same output)
- Explicit logic (no hidden side effects)
- Readability over brevity
- Zero external dependencies

Functional Requirements:
1. Add Task
   - Each task must have:
     - Unique ID (auto-increment or UUID)
     - Title (required, non-empty)
     - Optional description
     - Completion status (default: incomplete)

2. View Tasks
   - Display all tasks in a readable list
   - Clearly show ID, title, and completion status
   - Handle empty list gracefully

3. Update Task
   - Update title and/or description
   - Validate task existence before updating
   - Do NOT silently fail

4. Delete Task
   - Delete by task ID
   - Confirm existence before deletion

5. Mark Task as Complete / Incomplete
   - Toggle completion state
   - Explicit feedback after action

Non-Functional Requirements:
- No file system usage
- No database
- No async code
- No classes unless justified (functions preferred)
- No global mutable state without explanation
- Clear separation of concerns (menu logic vs task logic)

Error Handling Standards:
- Invalid input must be handled explicitly
- Program must never crash on bad user input
- User must always receive a clear error message

Code Quality Standards:
- Meaningful variable and function names
- Consistent formatting (PEP8)
- Inline comments ONLY where logic is non-obvious
- No dead code
- No unused variables or imports

CLI UX Standards:
- Clear menu options
- Loop-based interaction until user exits
- Explicit success and failure messages
- No confusing shortcuts or hidden commands

Constraints:
- Single Python file
- In-memory lifecycle: data resets on program restart
- Code must be beginner-readable but professional-grade

Out of Scope (STRICT):
- File saving
- Databases
- Web frameworks
- GUI
- AI features
- Authentication
- Testing frameworks (manual testing only)

Success Criteria:
- All listed features work correctly
- No unhandled exceptions
- Code can be extended later for Phase II (FastAPI + DB)
- Logic is clean enough to migrate to backend without rewrite
```

## Response snapshot

A constitution document has been created for the Todo Application project. The constitution includes:

- Six core principles: Simplicity Over Cleverness, Deterministic Behavior, Explicit Logic, Zero External Dependencies, Input Validation and Error Handling, and In-Memory Storage Only
- Additional constraints covering technology stack, functional requirements, and code quality standards
- Development workflow guidelines for error handling, CLI UX, and testing
- Governance rules for code contributions and reviews

The constitution enforces all the requirements specified, including single-file implementation, in-memory storage, zero external dependencies, and proper error handling.

## Outcome

- ✅ Impact: Created foundational governance document for the todo application project
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with project-specific principles
- 🔁 Next prompts: Implement the todo application according to the constitution
- 🧠 Reflection: The constitution captures all requirements and constraints from the user specification

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing the todo application features according to the constitution