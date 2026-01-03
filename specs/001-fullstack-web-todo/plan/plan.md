# Implementation Plan: Phase II — Full-Stack Web Todo Application

**Feature**: 001-fullstack-web-todo
**Created**: 2026-01-03
**Status**: Draft
**Plan Version**: 1.0.0

## Technical Context

**Backend Stack**: FastAPI for API server, SQLModel for ORM, Neon PostgreSQL for database
**Frontend Stack**: Next.js for client application
**Development Approach**: Backend-first with clean API-first architecture
**Repository Structure**: Separate `/backend` and `/frontend` directories
**Data Model**: Task entity with id, title (required), description (optional), is_completed (boolean), created_at (timestamp)
**API Protocol**: REST with JSON over HTTP
**Environment Management**: .env files for configuration

**Unknowns**:
- Neon PostgreSQL connection string format [NEEDS CLARIFICATION]
- Next.js project setup specifics [NEEDS CLARIFICATION]
- CORS configuration requirements [NEEDS CLARIFICATION]

## Constitution Check

This implementation plan complies with the Phase II Constitution:

✅ **Backend as Single Source of Truth**: All data and business logic will reside in the FastAPI backend
✅ **Frontend is Stateless and Dumb**: Next.js frontend will only handle UI and API calls
✅ **Business Logic in Backend Only**: All validation and business rules in FastAPI, not frontend
✅ **Database Schema Stability**: Task model schema will be frozen early with required fields
✅ **Explicit REST API Design**: Clear, predictable endpoints with proper HTTP codes
✅ **Production Realism Over Tutorial Shortcuts**: Proper error handling and configuration management

**Gates**:
- [ ] Backend API endpoints designed before frontend implementation
- [ ] Database schema finalized before implementation
- [ ] Environment variables defined for all configurations
- [ ] No business logic in frontend layer

## Phase 0: Research & Analysis

### Research Tasks

1. **Neon PostgreSQL Integration**
   - Research connection string format for Neon PostgreSQL
   - Determine best practices for connection pooling
   - Identify potential issues with Neon-specific features

2. **Next.js Architecture Planning**
   - Determine optimal project structure for API consumption
   - Identify state management approaches
   - Plan component architecture

3. **FastAPI-SQLModel Integration**
   - Research best practices for SQLModel with FastAPI
   - Determine session management patterns
   - Plan validation and error handling approaches

### Research Outcomes

**Decision**: Use async SQLAlchemy with SQLModel for database operations
**Rationale**: Provides async support that works well with FastAPI and Neon's connection model
**Alternatives considered**: Sync SQLAlchemy, raw asyncpg

**Decision**: Implement dependency injection for database sessions
**Rationale**: Follows FastAPI best practices and ensures proper session lifecycle
**Alternatives considered**: Global session objects, manual session creation

**Decision**: Use environment-based configuration for all settings
**Rationale**: Ensures proper separation of configuration from code
**Alternatives considered**: Hardcoded values, inline configuration

## Phase 1: Architecture & Design

### Data Model Design

**Entity: Task**
- `id` (Integer, Primary Key, Auto-generated)
- `title` (String, Required, Max 255 chars)
- `description` (String, Optional, Max 1000 chars)
- `is_completed` (Boolean, Default: False)
- `created_at` (DateTime, Auto-generated)

**Validation Rules**:
- Title must not be empty
- Title length must be 1-255 characters
- Description length must be 0-1000 characters

### API Contract Design

**Endpoint: POST /tasks**
- Request: `{"title": "string", "description": "string"}`
- Response: `{"id": int, "title": "string", "description": "string", "is_completed": false, "created_at": "datetime"}`
- Status Codes: 201 (Created), 422 (Validation Error), 500 (Server Error)

**Endpoint: GET /tasks**
- Request: (no body)
- Response: `[{"id": int, "title": "string", "description": "string", "is_completed": bool, "created_at": "datetime"}]`
- Status Codes: 200 (OK), 500 (Server Error)

**Endpoint: PUT /tasks/{id}**
- Request: `{"title": "string", "description": "string"}`
- Response: `{"id": int, "title": "string", "description": "string", "is_completed": bool, "created_at": "datetime"}`
- Status Codes: 200 (OK), 404 (Not Found), 422 (Validation Error), 500 (Server Error)

**Endpoint: DELETE /tasks/{id}**
- Request: (no body)
- Response: (no body)
- Status Codes: 204 (No Content), 404 (Not Found), 500 (Server Error)

**Endpoint: PATCH /tasks/{id}/toggle**
- Request: (no body)
- Response: `{"id": int, "title": "string", "description": "string", "is_completed": bool, "created_at": "datetime"}`
- Status Codes: 200 (OK), 404 (Not Found), 500 (Server Error)

### Repository Structure
```
todo-app/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── database/
│   │   └── api/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── services/
│   └── .env
├── specs/
├── README.md
└── CLAUDE.md
```

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string for Neon
- `BACKEND_CORS_ORIGINS`: Comma-separated list of allowed origins
- `SECRET_KEY`: Secret key for security (not used in Phase II but reserved)

## Phase 2: Implementation Strategy

### Backend Implementation Order
1. Set up project structure and dependencies
2. Implement database models and session management
3. Create Pydantic schemas for request/response validation
4. Implement API routes with proper error handling
5. Test endpoints manually using curl/httpie
6. Deploy and verify data persistence

### Frontend Implementation Order
1. Set up Next.js project structure
2. Create API service layer to interact with backend
3. Implement task list component
4. Create task form component
5. Implement task update/delete functionality
6. Add loading and error state handling
7. Test full user flows

### Verification Strategy
- Manual API testing using curl or HTTP client
- Frontend-end-to-end functionality verification
- Database persistence verification across restarts
- Error handling verification
- Cross-browser compatibility (if needed)

## Risk Assessment

**High Risk Items**:
- Database connection issues with Neon
- CORS configuration between frontend and backend
- Data validation edge cases

**Mitigation Strategies**:
- Thorough testing of database connectivity early
- Proper CORS configuration during backend setup
- Comprehensive validation testing for all endpoints

## Success Criteria Verification

Each success criterion from the specification will be verified:
- [ ] All 5 core features work end-to-end
- [ ] Data persists in Neon DB across restarts
- [ ] Backend exposes clear REST APIs with proper HTTP codes
- [ ] Frontend reflects backend state accurately
- [ ] No business logic in frontend
- [ ] Codebase extendable for Phase III