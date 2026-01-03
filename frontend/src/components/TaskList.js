// TaskList component to display all tasks
import React, { useState, useEffect } from 'react';
import { taskService } from '../services/api';

const TaskList = ({ onTaskUpdate, onTaskDelete, onToggleCompletion }) => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const data = await taskService.getTasks();
      setTasks(data);
      setError(null);
    } catch (err) {
      setError('Failed to load tasks');
      console.error('Error loading tasks:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading tasks...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="task-list">
      <h2>My Tasks</h2>
      {tasks.length === 0 ? (
        <p>No tasks yet. Add one to get started!</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id} className={`task-item ${task.is_completed ? 'completed' : ''}`}>
              <div className="task-info">
                <h3>{task.title}</h3>
                {task.description && <p>{task.description}</p>}
                <div className="task-meta">
                  <small>Created: {new Date(task.created_at).toLocaleString()}</small>
                  <span className={`status ${task.is_completed ? 'completed' : 'pending'}`}>
                    {task.is_completed ? 'Completed' : 'Pending'}
                  </span>
                </div>
              </div>
              <div className="task-actions">
                <button
                  onClick={() => onToggleCompletion(task.id, !task.is_completed)}
                  className={`toggle-btn ${task.is_completed ? 'mark-incomplete' : 'mark-complete'}`}
                >
                  {task.is_completed ? 'Mark Incomplete' : 'Mark Complete'}
                </button>
                <button
                  onClick={() => onTaskUpdate(task)}
                  className="edit-btn"
                >
                  Edit
                </button>
                <button
                  onClick={() => onTaskDelete(task.id)}
                  className="delete-btn"
                >
                  Delete
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TaskList;