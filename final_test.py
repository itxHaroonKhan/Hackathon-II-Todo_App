#!/usr/bin/env python3
"""
Final test to verify all 5 basic features of the todo app are working
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from todo_app import add_task, get_all_tasks, update_task, delete_task, toggle_task_status, display_tasks

print("=== FINAL VERIFICATION TEST ===")
print("Testing all 5 basic features of the Todo Application...\n")

# Test 1: Add Task
print("1. Testing ADD TASK feature:")
result = add_task("Test task for verification", "This is a test description")
if result:
    print(f"   [PASS] Add task successful: {result['title']}")
    task_id = result['id']
else:
    print("   [FAIL] Add task failed")
    sys.exit(1)

# Test 2: View Tasks
print("\n2. Testing VIEW TASKS feature:")
all_tasks = get_all_tasks()
if len(all_tasks) > 0:
    print(f"   [PASS] View tasks successful: Found {len(all_tasks)} task(s)")
    display_tasks()
else:
    print("   [FAIL] View tasks failed: No tasks found")
    sys.exit(1)

# Test 3: Update Task
print("\n3. Testing UPDATE TASK feature:")
result = update_task(task_id, title="Updated test task", description="Updated description")
if result:
    print(f"   [PASS] Update task successful: {result['title']}")
else:
    print("   [FAIL] Update task failed")
    sys.exit(1)

# Test 4: Mark Task Complete/Incomplete
print("\n4. Testing MARK TASK COMPLETE feature:")
result = toggle_task_status(task_id)
if result:
    print(f"   [PASS] Mark task complete successful: Task {task_id} is now {'completed' if result['is_completed'] else 'incomplete'}")
else:
    print("   [FAIL] Mark task complete failed")
    sys.exit(1)

# Toggle back to incomplete to test both states
result = toggle_task_status(task_id)
if result:
    print(f"   [PASS] Mark task incomplete successful: Task {task_id} is now {'completed' if result['is_completed'] else 'incomplete'}")

# Test 5: Delete Task
print("\n5. Testing DELETE TASK feature:")
result = delete_task(task_id)
if result:
    print(f"   [PASS] Delete task successful: Task {task_id} deleted")
else:
    print("   [FAIL] Delete task failed")
    sys.exit(1)

# Verify deletion
print("\n6. Verifying task was deleted:")
all_tasks = get_all_tasks()
if len(all_tasks) == 0:
    print("   [PASS] Task deletion confirmed: Task list is now empty")
else:
    print(f"   [FAIL] Task deletion failed: Still have {len(all_tasks)} task(s)")
    sys.exit(1)

print("\n=== ALL TESTS PASSED ===")
print("[PASS] Add Task - WORKING")
print("[PASS] View Tasks - WORKING")
print("[PASS] Update Task - WORKING")
print("[PASS] Delete Task - WORKING")
print("[PASS] Mark Task Complete/Incomplete - WORKING")
print("\nThe In-Memory Console Todo Application is fully functional!")