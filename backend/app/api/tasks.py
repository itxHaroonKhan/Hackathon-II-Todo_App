from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from typing import List

from app.models.task import Task, TaskCreate, TaskUpdate, TaskRead
from app.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    """
    Create a new task with the provided title and optional description.
    The new task will have is_completed set to False by default and created_at set to current time.
    """
    db_task = Task.model_validate(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.get("/", response_model=List[TaskRead])
def read_tasks(session: Session = Depends(get_session)):
    """
    Get all tasks in the system.
    Returns a list of all tasks with their details.
    """
    statement = select(Task)
    results = session.execute(statement)
    tasks = results.scalars().all()
    return tasks


@router.get("/{task_id}", response_model=TaskRead)
def read_task(task_id: int, session: Session = Depends(get_session)):
    """
    Get a specific task by its ID.
    Returns the task details if found, 404 if not found.
    """
    statement = select(Task).where(Task.id == task_id)
    result = session.execute(statement)
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task: TaskUpdate, session: Session = Depends(get_session)):
    """
    Update an existing task with new information.
    Only provided fields will be updated, others will remain unchanged.
    Returns 404 if the task doesn't exist.
    """
    statement = select(Task).where(Task.id == task_id)
    result = session.execute(statement)
    db_task = result.scalar_one_or_none()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update only the fields that are provided
    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.is_completed is not None:
        db_task.is_completed = task.is_completed

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    """
    Delete a task by its ID.
    Returns 204 No Content on successful deletion, 404 if not found.
    """
    statement = select(Task).where(Task.id == task_id)
    result = session.execute(statement)
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(task)
    session.commit()


@router.patch("/{task_id}/toggle", response_model=TaskRead)
def toggle_task_completion(task_id: int, session: Session = Depends(get_session)):
    """
    Toggle the completion status of a task.
    If the task is completed, it becomes incomplete, and vice versa.
    Returns 404 if the task doesn't exist.
    """
    statement = select(Task).where(Task.id == task_id)
    result = session.execute(statement)
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Toggle the completion status
    task.is_completed = not task.is_completed

    session.add(task)
    session.commit()
    session.refresh(task)

    return task