"""
Test script to verify the todo application functions work correctly
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the functions from todo_app
from todo_app import add_task, get_all_tasks, get_task_by_id, update_task, delete_task, toggle_task_status, display_tasks

print("Testing Todo Application Functions...")

# Test 1: Add a task
print("\n1. Testing add_task function:")
result = add_task("Test Task 1", "This is a test task")
print(f"Result: {result}")

# Test 2: Add another task
print("\n2. Adding another task:")
result = add_task("Test Task 2")
print(f"Result: {result}")

# Test 3: View all tasks
print("\n3. Testing get_all_tasks function:")
all_tasks = get_all_tasks()
print(f"Number of tasks: {len(all_tasks)}")
for task in all_tasks:
    print(f"  - ID: {task['id']}, Title: {task['title']}, Completed: {task['is_completed']}")

# Test 4: Get task by ID
print("\n4. Testing get_task_by_id function:")
task = get_task_by_id(1)
print(f"Task with ID 1: {task}")

# Test 5: Update a task
print("\n5. Testing update_task function:")
result = update_task(1, title="Updated Test Task 1", description="Updated description")
print(f"Update result: {result}")

# Test 6: Toggle task status
print("\n6. Testing toggle_task_status function:")
result = toggle_task_status(1)
print(f"Toggle result: {result}")

# Test 7: Display tasks
print("\n7. Testing display_tasks function:")
display_tasks()

# Test 8: Delete a task
print("\n8. Testing delete_task function:")
result = delete_task(2)
print(f"Delete result: {result}")

# Test 9: View tasks after deletion
print("\n9. Tasks after deletion:")
display_tasks()

print("\nAll tests completed successfully!")