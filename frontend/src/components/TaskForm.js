// TaskForm component for adding and updating tasks
import React, { useState } from 'react';
import { taskService } from '../services/api';

const TaskForm = ({ onTaskCreated, onTaskUpdated, initialTask = null }) => {
  const [title, setTitle] = useState(initialTask?.title || '');
  const [description, setDescription] = useState(initialTask?.description || '');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);

  const isUpdateForm = !!initialTask;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      const taskData = { title, description };

      if (isUpdateForm) {
        // Update existing task
        await taskService.updateTask(initialTask.id, taskData);
        onTaskUpdated();
      } else {
        // Create new task
        await taskService.createTask(taskData);
        onTaskCreated();
      }

      // Reset form
      setTitle('');
      setDescription('');
    } catch (err) {
      setError('Failed to save task');
      console.error('Error saving task:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="task-form">
      <h2>{isUpdateForm ? 'Update Task' : 'Add New Task'}</h2>
      {error && <div className="error">Error: {error}</div>}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="title">Title *</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            disabled={isSubmitting}
            placeholder="Task title"
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            disabled={isSubmitting}
            placeholder="Task description (optional)"
            rows="3"
          />
        </div>

        <button
          type="submit"
          disabled={isSubmitting || !title.trim()}
          className="submit-btn"
        >
          {isSubmitting
            ? (isUpdateForm ? 'Updating...' : 'Creating...')
            : (isUpdateForm ? 'Update Task' : 'Create Task')}
        </button>
      </form>
    </div>
  );
};

export default TaskForm;