---
id: PHR-0004
title: Phase II Task Breakdown
stage: tasks
date: 2026-01-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-fullstack-web-todo
branch: 001-fullstack-web-todo
user: itxHaroonKhan
command: /sp.tasks
labels: ["tasks", "todo", "fullstack", "breakdown"]
links:
  spec: specs/001-fullstack-web-todo/spec.md
  plan: specs/001-fullstack-web-todo/plan/plan.md
  tasks: specs/001-fullstack-web-todo/tasks/tasks.md
  adr: null
  pr: null
files:
 - specs/001-fullstack-web-todo/tasks/tasks.md
 - specs/001-fullstack-web-todo/checklists/tasks.md
 - history/prompts/001-fullstack-web-todo/phr-0004-task-breakdown.md
tests:
 - none
---

## Prompt

Phase II — Full-Stack Web Todo Application

Global Constraints (STRICT):
- All 5 core Todo features must be implemented
- FastAPI backend owns all business logic
- SQLModel + Neon DB mandatory for persistence
- Next.js frontend consumes APIs only
- Spec-driven development using Claude Code + Spec-Kit Plus
- No manual coding
- Scope strictly Phase II
- No AI, auth, Docker, or background jobs

Atomic Tasks (Ordered):

TASK 1: Repository Setup
- Create root repo with:
  - /backend
  - /frontend
  - /specs_history
  - README.md
  - CLAUDE.md
- Ensure frontend and backend separation

Acceptance Criteria:
- Repo structure matches Phase II specification

---

TASK 2: Environment & DB Setup
- Configure Neon PostgreSQL
- Create `.env` for DATABASE_URL
- Implement SQLModel engine and session management in `/backend/database.py`

Acceptance Criteria:
- Backend can connect to Neon DB
- No code written for API yet

---

TASK 3: Task Data Model Implementation
- Define Task model using SQLModel:
  - id (primary key)
  - title (required)
  - description (optional)
  - is_completed (boolean)
  - created_at (timestamp)
- Freeze schema and document decisions

Acceptance Criteria:
- Task model ready for CRUD operations

---

TASK 4: Backend API Endpoint Design
- Define REST endpoints contract:
  - POST   /tasks
  - GET    /tasks
  - PUT    /tasks/{id}
  - DELETE /tasks/{id}
  - PATCH  /tasks/{id}/toggle
- Define request/response schema
- Plan error handling (404, 400, 422)

Acceptance Criteria:
- Backend API contract documented
- Ready for implementation

---

TASK 5: Implement Backend CRUD Endpoints
- Implement all 5 endpoints in FastAPI
- Apply SQLModel validation
- Ensure proper HTTP status codes

Acceptance Criteria:
- Endpoints functional independently
- Can be tested via curl or Postman

---

TASK 6: Backend Verification
- Test all endpoints manually:
  - CRUD correctness
  - Error handling
  - Data persistence in Neon DB

Acceptance Criteria:
- Backend validated, no dependency on frontend

---

TASK 7: Frontend Architecture Planning
- Define Next.js structure:
  - Pages / app router
  - Components
  - API service layer (e.g., fetch/axios)
- Decide data fetching and state management

Acceptance Criteria:
- Frontend structure ready for implementation

---

TASK 8: Implement Frontend UI
- Create UI for:
  - Adding tasks
  - Listing tasks with status
  - Updating tasks
  - Deleting tasks
  - Toggling completion
- Connect UI to backend via REST API
- Handle loading & error states

Acceptance Criteria:
- Frontend fully functional and decoupled
- No business logic in frontend

---

TASK 9: End-to-End Testing
- Test complete flow:
  - Add, view, update, delete, toggle
  - Persistent storage verification
  - Edge cases & error handling

Acceptance Criteria:
- Application works as intended
- Frontend reflects backend accurately

---

TASK 10: Documentation
- Update README.md:
  - Backend & frontend setup
  - Environment variables
  - Run instructions
- Update CLAUDE.md:
  - Spec-driven workflow instructions
  - How to use Claude Code for Phase II

Acceptance Criteria:
- Complete documentation ready for review

---

TASK 11: Manual Review Before Completion
- Ensure all success criteria from /sp.specify are met
- Confirm code is clean, extendable for Phase III
- Verify repository structure

Acceptance Criteria:
- Phase II ready for grading/review
- No skipped tasks

## Response snapshot

Created comprehensive task breakdown with 11 detailed tasks for Phase II Full-Stack Web Todo Application implementation.

## Outcome

- ✅ Impact: Created complete task breakdown with detailed implementation steps and acceptance criteria
- 🧪 Tests: none
- 📁 Files: specs/001-fullstack-web-todo/tasks/tasks.md, specs/001-fullstack-web-todo/checklists/tasks.md
- 🔁 Next prompts: /sp.implement to execute the implementation
- 🧠 Reflection: Task breakdown follows spec-driven approach with proper dependencies and priorities

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): None needed