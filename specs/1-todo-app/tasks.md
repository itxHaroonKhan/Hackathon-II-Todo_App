---
description: "Task list for In-Memory Python Console Todo Application"
---

# Tasks: In-Memory Python Console Todo Application

**Input**: Design documents from `/specs/1-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create repository structure per implementation plan: constitution file, /specs_history directory, /src directory, README.md, CLAUDE.md
- [X] T002 Create /src directory for Python source code
- [X] T003 [P] Create README.md with setup instructions
- [X] T004 [P] Create CLAUDE.md with Claude Code usage instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Define Task data model with id (unique, immutable), title (required, non-empty string), description (optional string), is_completed (boolean)
- [X] T006 Implement in-memory storage container using list or dict for tasks
- [X] T007 Create base task management functions in src/todo_app.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks to their todo list with title and optional description

**Independent Test**: The application can be tested by adding a new task with a title and optional description, and the task should appear in the task list with a unique ID and default incomplete status.

### Implementation for User Story 1

- [X] T008 Implement add_task function in src/todo_app.py that accepts title and description parameters
- [X] T009 Add input validation for title (must not be empty) in add_task function
- [X] T010 Implement unique ID generation for new tasks in add_task function
- [X] T011 Store new task in memory with default is_completed=False status
- [X] T012 Display success message after task creation
- [X] T013 Handle and display error for empty or invalid title input

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1) 🎯 MVP

**Goal**: Display all tasks with their IDs, titles, and completion status clearly

**Independent Test**: The application can be tested by adding some tasks and then viewing the task list, which should display all tasks with their unique IDs, titles, and completion status clearly.

### Implementation for User Story 2

- [X] T014 Implement get_all_tasks function in src/todo_app.py to retrieve all tasks
- [X] T015 Create display_tasks function in src/todo_app.py to format and show tasks
- [X] T016 Show ID, title, and completion status (Pending/Done) for each task
- [X] T017 Handle empty task list with appropriate message
- [X] T018 Format output in a readable CLI format

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Allow users to update the title or description of an existing task

**Independent Test**: The application can be tested by updating an existing task's title or description and then viewing the task to confirm the changes were saved.

### Implementation for User Story 3

- [X] T019 Implement get_task_by_id function in src/todo_app.py to find tasks by ID
- [X] T020 Implement update_task function in src/todo_app.py to modify title/description
- [X] T021 Add validation to ensure task exists before updating
- [X] T022 Add validation to ensure title is not empty when provided
- [X] T023 Return updated task information after successful update

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Allow users to delete tasks that they no longer need

**Independent Test**: The application can be tested by deleting an existing task and then viewing the task list to confirm the task was removed.

### Implementation for User Story 4

- [X] T024 Implement delete_task function in src/todo_app.py to remove tasks by ID
- [X] T025 Add validation to ensure task exists before deletion
- [X] T026 Remove task from in-memory storage
- [X] T027 Provide explicit feedback after deletion
- [X] T028 Handle invalid task ID gracefully

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Allow users to mark tasks as complete when finished and toggle back to incomplete

**Independent Test**: The application can be tested by marking a task as complete and then viewing the task list to confirm the status change, and then marking it as incomplete again.

### Implementation for User Story 5

- [X] T029 Implement toggle_task_status function in src/todo_app.py to change completion status
- [X] T030 Add validation to ensure task exists before toggling status
- [X] T031 Toggle is_completed field between True and False
- [X] T032 Provide explicit feedback after status change
- [X] T033 Handle invalid task ID gracefully

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: User Story 6 - CLI Menu & Control Flow (Priority: P1) 🎯 MVP

**Goal**: Implement loop-based menu system for user interaction

**Independent Test**: The application runs continuously, presenting menu options and routing user input to appropriate functions.

### Implementation for User Story 6

- [X] T034 Implement display_menu function in src/todo_app.py to show available options
- [X] T035 Create run_application function with main loop in src/todo_app.py
- [X] T036 Implement handle_user_input function to route menu choices to appropriate functions
- [X] T037 Add proper input validation and error handling for menu selections
- [X] T038 Implement clean exit functionality

**Checkpoint**: At this point, the complete application should be functional with CLI interface

---

## Phase 9: Polish & Code Quality

**Purpose**: Final improvements and quality assurance

- [X] T039 Ensure PEP8 compliance for all code in src/todo_app.py
- [X] T040 Verify meaningful function and variable naming throughout
- [X] T041 Remove any unused variables or imports
- [X] T042 Add minimal comments only where logic is non-obvious
- [X] T043 Ensure clear separation of concerns (business logic vs CLI logic)
- [X] T044 Test all features work together as expected
- [X] T045 Validate application follows constitution requirements

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable
- **User Story 6 (P1)**: Can start after Foundational (Phase 2) - Will integrate all other user stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

## Implementation Strategy

### MVP First (User Stories 1, 2, 6 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. Complete Phase 8: User Story 6 (CLI Interface)
6. **STOP and VALIDATE**: Test basic add/view functionality with CLI interface
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add US1 (Add Task) → Test independently → Deploy/Demo
3. Add US2 (View Tasks) → Test independently → Deploy/Demo
4. Add US6 (CLI Interface) → Test together → Deploy/Demo (MVP!)
5. Add US3 (Update Task) → Test independently → Deploy/Demo
6. Add US4 (Delete Task) → Test independently → Deploy/Demo
7. Add US5 (Mark Complete) → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories