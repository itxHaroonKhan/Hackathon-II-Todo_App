# Phase II — Full-Stack Web Todo Application

## Project Overview
This is a full-stack web todo application built with a clean API-first architecture. The backend uses FastAPI with SQLModel for data persistence in Neon PostgreSQL, while the frontend is built with Next.js that consumes backend APIs only.

## Architecture
- **Backend**: FastAPI + SQLModel + PostgreSQL (Neon)
- **Frontend**: Next.js
- **Database**: Neon PostgreSQL
- **Communication**: REST API with JSON

## Features
- Add tasks with title and optional description
- View all tasks with completion status indicators
- Update task details
- Delete tasks permanently
- Toggle task completion status
- All data persists in Neon PostgreSQL database

## Tech Stack
- Python 3.9+ for backend
- Node.js 18+ for frontend
- FastAPI for backend API framework
- SQLModel for ORM
- Next.js for frontend framework
- Neon PostgreSQL for database
- Axios for HTTP client in frontend

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory: `cd backend`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix/Mac: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create environment file: `cp .env.example .env`
6. Update `.env` with your Neon PostgreSQL connection string
7. Start the backend: `uvicorn app.main:app --reload`

### Frontend Setup
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Create environment file: `cp .env.example .env`
4. Update `.env` with backend API URL
5. Start the frontend: `npm run dev`

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: PostgreSQL connection string for Neon database
- `BACKEND_CORS_ORIGINS`: Comma-separated list of allowed origins (default: http://localhost:3000)

### Frontend (.env)
- `NEXT_PUBLIC_API_URL`: Backend API URL (default: http://localhost:8000)

## API Endpoints
- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task
- `PATCH /tasks/{id}/toggle` - Toggle task completion status

## Running the Application
1. Start the backend server first: `cd backend && uvicorn app.main:app --reload`
2. In a separate terminal, start the frontend server: `cd frontend && npm run dev`
3. The backend API will be available at http://localhost:8000
4. The frontend application will be available at http://localhost:3000

## Project Structure
```
todo-app/
├── backend/                 # FastAPI backend application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # Main application file
│   │   ├── models/          # SQLModel data models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── database/        # Database configuration
│   │   └── api/             # API routes
│   ├── requirements.txt     # Backend dependencies
│   └── .env                 # Backend environment variables
├── frontend/                # Next.js frontend application
│   ├── package.json         # Frontend dependencies
│   ├── src/
│   │   ├── pages/           # Next.js pages
│   │   ├── components/      # React components
│   │   └── services/        # API service layer
│   └── .env                 # Frontend environment variables
├── specs/                   # Specification files
│   └── 001-fullstack-web-todo/
│       ├── spec.md          # Feature specification
│       ├── plan.md          # Implementation plan
│       ├── tasks.md         # Task breakdown
│       └── checklists/      # Quality checklists
├── specs_history/           # Historical specs
├── README.md                # Project documentation
├── CLAUDE.md                # Claude Code usage instructions
└── other project files
```

## API Documentation
The API follows REST principles and returns JSON responses. All endpoints return appropriate HTTP status codes:
- 200: Success for GET requests
- 201: Created for POST requests
- 204: No Content for DELETE requests
- 404: Not Found when a resource doesn't exist
- 422: Validation Error for invalid input
- 500: Internal Server Error for unexpected errors