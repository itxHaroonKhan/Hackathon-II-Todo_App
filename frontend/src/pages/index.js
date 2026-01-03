// Main page for the Todo application
import React, { useState, useCallback } from 'react';
import TaskList from '../components/TaskList';
import TaskForm from '../components/TaskForm';
import { taskService } from '../services/api';

const TodoApp = () => {
  const [tasks, setTasks] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [loading, setLoading] = useState(false);

  // Callbacks for handling tasks
  const handleTaskCreated = useCallback(async () => {
    setShowForm(false);
    // Refresh tasks after creation
    try {
      const data = await taskService.getTasks();
      setTasks(data);
    } catch (err) {
      console.error('Error refreshing tasks after creation:', err);
    }
  }, []);

  const handleTaskUpdated = useCallback(async () => {
    setEditingTask(null);
    setShowForm(false);
    // Refresh tasks after update
    try {
      const data = await taskService.getTasks();
      setTasks(data);
    } catch (err) {
      console.error('Error refreshing tasks after update:', err);
    }
  }, []);

  const handleToggleCompletion = useCallback(async (taskId, newStatus) => {
    try {
      await taskService.toggleTaskCompletion(taskId);
      // Refresh tasks after toggle
      const data = await taskService.getTasks();
      setTasks(data);
    } catch (err) {
      console.error('Error toggling task completion:', err);
    }
  }, []);

  const handleDeleteTask = useCallback(async (taskId) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        setLoading(true);
        await taskService.deleteTask(taskId);
        // Refresh tasks after deletion
        const data = await taskService.getTasks();
        setTasks(data);
      } catch (err) {
        console.error('Error deleting task:', err);
      } finally {
        setLoading(false);
      }
    }
  }, []);

  const handleEditTask = (task) => {
    setEditingTask(task);
    setShowForm(true);
  };

  return (
    <div className="todo-app">
      <header>
        <h1>Todo Application</h1>
      </header>

      <main>
        <div className="controls">
          <button
            onClick={() => {
              setEditingTask(null);
              setShowForm(!showForm);
            }}
            className="add-task-btn"
          >
            {showForm ? 'Cancel' : editingTask ? 'Cancel Edit' : 'Add New Task'}
          </button>
        </div>

        {showForm ? (
          <TaskForm
            initialTask={editingTask}
            onTaskCreated={handleTaskCreated}
            onTaskUpdated={handleTaskUpdated}
          />
        ) : null}

        <TaskList
          tasks={tasks}
          onTaskUpdate={handleEditTask}
          onTaskDelete={handleDeleteTask}
          onToggleCompletion={handleToggleCompletion}
        />

        {loading && <div className="loading-overlay">Processing...</div>}
      </main>

      <style jsx>{`
        .todo-app {
          max-width: 800px;
          margin: 0 auto;
          padding: 20px;
          font-family: Arial, sans-serif;
        }

        header {
          text-align: center;
          margin-bottom: 30px;
        }

        header h1 {
          color: #333;
          margin: 0;
        }

        .controls {
          margin-bottom: 20px;
          text-align: center;
        }

        .add-task-btn {
          background-color: #007bff;
          color: white;
          border: none;
          padding: 10px 20px;
          border-radius: 4px;
          cursor: pointer;
          font-size: 16px;
        }

        .add-task-btn:hover {
          background-color: #0056b3;
        }

        .loading-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: rgba(0, 0, 0, 0.5);
          display: flex;
          justify-content: center;
          align-items: center;
          color: white;
          font-size: 18px;
          z-index: 1000;
        }
      `}</style>
    </div>
  );
};

export default TodoApp;