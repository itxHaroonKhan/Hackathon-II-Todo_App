# Quickstart Guide: Phase II — Full-Stack Web Todo Application

## Prerequisites

- Python 3.9+ for backend development
- Node.js 18+ for frontend development
- PostgreSQL client tools
- Git for version control

## Environment Setup

### Backend (FastAPI)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
cp .env.example .env
```

5. Update `.env` with your Neon PostgreSQL connection string:
```bash
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
```

6. Run the application:
```bash
uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

### Frontend (Next.js)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Update `.env` with backend API URL:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

5. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

### Tasks API

- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task
- `PATCH /tasks/{id}/toggle` - Toggle task completion status

## Development Workflow

1. Start the backend server
2. In a separate terminal, start the frontend server
3. The frontend will automatically connect to the backend API
4. Make changes and test functionality

## Testing the API

You can test the API endpoints directly using curl:

```bash
# Get all tasks
curl http://localhost:8000/tasks

# Create a new task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test task", "description": "A test task"}'
```

## Database Migrations

The application will automatically create the necessary database tables when it starts up. No manual migration steps are required for Phase II.