---
id: PHR-0003
title: Phase II Plan Creation
stage: plan
date: 2026-01-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-fullstack-web-todo
branch: 001-fullstack-web-todo
user: itxHaroonKhan
command: /sp.plan
labels: ["plan", "todo", "fullstack", "architecture"]
links:
  spec: specs/001-fullstack-web-todo/spec.md
  plan: specs/001-fullstack-web-todo/plan/plan.md
  adr: null
  pr: null
files:
 - specs/001-fullstack-web-todo/plan/plan.md
 - specs/001-fullstack-web-todo/plan/research.md
 - specs/001-fullstack-web-todo/plan/data-model.md
 - specs/001-fullstack-web-todo/plan/contracts/openapi.yaml
 - specs/001-fullstack-web-todo/plan/quickstart.md
tests:
 - none
---

## Prompt

Phase II — Full-Stack Web Todo Application

Objective:
Implement Phase II as a production-style full-stack web application by evolving Phase I logic into a clean API-first system using FastAPI, SQLModel, Neon PostgreSQL, and Next.js — strictly via spec-driven development.

Authority:
This plan is governed by:
- Phase II /sp.constitution
- Phase II /sp.specify

Deviation from this plan is NOT allowed.

Mandatory Requirements (NON-NEGOTIABLE):
- All 5 Todo features must work end-to-end
- Backend-first development
- Persistent storage using Neon DB
- Clean separation between frontend and backend
- No manual coding (Claude Code + Spec-Kit Plus only)

---

Step 1: Scope & Spec Alignment
- Re-read Phase II Constitution and Specify
- Confirm Phase II scope only
- Explicitly lock out:
  - AI features
  - Auth
  - Docker / Kubernetes
  - Kafka / background jobs

Deliverable:
- Internal confirmation of scope
- No code generated

---

Step 2: Repository Structure Planning
- Define top-level structure:
  - /backend
  - /frontend
  - /specs_history
  - README.md
  - CLAUDE.md
- Ensure frontend and backend are fully decoupled

Deliverable:
- Approved repository layout
- No implementation yet

---

Step 3: Data Model Finalization (CRITICAL)
- Define Task model using SQLModel:
  - id (primary key)
  - title (required)
  - description (optional)
  - is_completed (boolean)
  - created_at (timestamp)
- Freeze schema early
- Document model decisions

Deliverable:
- Final Task model spec
- No DB writes yet

---

Step 4: Database & Environment Setup
- Configure Neon PostgreSQL
- Define environment variables (.env):
  - DATABASE_URL
- Implement SQLModel engine and session management
- Verify DB connectivity

Deliverable:
- Working database connection
- No API routes yet

---

Step 5: Backend API Design
- Design REST endpoints:
  - POST   /tasks
  - GET    /tasks
  - PUT    /tasks/{id}
  - DELETE /tasks/{id}
  - PATCH  /tasks/{id}/toggle
- Define request/response schemas
- Define error handling strategy

Deliverable:
- API contract documented
- No frontend dependency

---

Step 6: Backend Implementation (FastAPI)
- Implement routes incrementally:
  1. Create task
  2. List tasks
  3. Update task
  4. Delete task
  5. Toggle completion
- Apply validation via SQLModel
- Ensure proper HTTP status codes

Deliverable:
- Fully working backend API
- Can be tested via curl / HTTP client

---

Step 7: Backend Manual Verification
- Manually test all endpoints
- Verify:
  - CRUD correctness
  - Error handling
  - Data persistence across restarts

Deliverable:
- Backend validated independently

---

Step 8: Frontend Architecture Planning
- Define Next.js structure:
  - Pages / App Router
  - Components
  - API service layer
- Decide data-fetching approach (fetch / axios)

Deliverable:
- Frontend architecture plan
- No UI yet

---

Step 9: Frontend Implementation (Next.js)
- Implement UI features:
  - Add task form
  - Task list view
  - Update task UI
  - Delete task action
  - Toggle completion
- Connect to backend via REST APIs
- Handle loading and error states

Deliverable:
- Fully functional frontend
- No backend logic duplicated

---

Step 10: End-to-End Integration Testing
- Verify frontend ↔ backend integration
- Confirm UI reflects backend state
- Test edge cases and failures

Deliverable:
- End-to-end working application

---

Step 11: Documentation
- Update README.md:
  - Backend setup
  - Frontend setup
  - Environment variables
- Update CLAUDE.md:
  - Spec-driven workflow
  - How to run Phase II

Deliverable:
- Complete, accurate documentation

---

Completion Criteria:
- Full CRUD works via web UI
- Data persists in Neon DB
- Frontend and backend are decoupled
- Codebase is ready for Phase III AI integration

Failure Conditions:
- Frontend contains business logic
- Backend depends on frontend
- Schema changes mid-implementation
- Scope creep beyond Phase II

## Response snapshot

Created comprehensive implementation plan for Phase II Full-Stack Web Todo Application with research, data model, API contracts, and quickstart guide.

## Outcome

- ✅ Impact: Created complete implementation plan with architecture, data model, and API contracts
- 🧪 Tests: none
- 📁 Files: specs/001-fullstack-web-todo/plan/plan.md, research.md, data-model.md, contracts/openapi.yaml, quickstart.md
- 🔁 Next prompts: /sp.tasks to create implementation tasks
- 🧠 Reflection: Plan follows spec-driven approach with clear architecture and compliance with constitution

## Evaluation notes (flywheel)

- Failure modes observed: PowerShell script not available on system, had to create plan manually
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create bash alternative to PowerShell script