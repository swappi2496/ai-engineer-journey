import json
import os

tasks_file = "tasks.json"

def load_tasks():
    #if tasks_file doesn't exist, return an empty list
    if not os.path.exists(tasks_file):
        return []
    #otherwise, open it and return json.load(f)
    with open(tasks_file, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    # open tasks_file for writing, json.dump(tasks, f, indent = 2)
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent = 2)

def add_task(tasks):
    text = input("Task description: ").strip()
    if not text:
        print("Empty task - not added.")
        return
    # calculate next id (max existing id +1, or 1 if empty)
    if tasks:
        next_id = max(task["id"] for task in tasks) +1
    else:
        next_id = 1
    # Append a new task dict {"id": ..., "text": ..., "done": false}
    new_task = {"id": next_id, "text": text, "done": False}
    tasks.append(new_task)
    print(f"Added : [{next_id}] {text}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet")
        return
    print()
    
    #Loop through tasks, print each as:
    # "[] 1. Buy groceries" for not-done
    # "[x] 2. call num" for done
    for task in tasks:
        marker = "[x]" if task["done"] else "[]"
        print(f"{marker} {task['id']}. {task['text']}")

def mark_complete(tasks):
    #show list, ask for id, set that task's done to true
    if not tasks:
        print("No task to mark.")
        return
    list_tasks(tasks)
    try:
        target_id = int(input("Enter task id to mark complete:"))
    except ValueError:
        print("Invalid id - must be a number")
        return
    
    for task in tasks:
        if task["id"] == target_id:
            task["done"] = True
            print(f"Marked complete: {task['text']}")
            return
    print(f'No task found with id {target_id}.')

def delete_task(tasks):
    #ask for a task id and remove it from the list.
    if not tasks:
        print("No tasks to delete")
        return
    list_tasks(tasks)

     # show list, ask for id, remove that task from list 

    try:
        target_id = int(input("Enter task id to delete:"))
    except ValueError:
        print("Invalid id - must be a number.")
        return
    
    for i, task in enumerate(tasks):
        if task["id"] == target_id:
            removed = tasks.pop(i)
            print(f"Deleted: {removed['text']}")
            return
    print(f"No task found with id {target_id}.")

def main():
    tasks = load_tasks()
    while True:
        print('\n--- TODO ---')
        print("1. Add 2. List 3. Mark Complete 4. Delete 5. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Good Bye.")
            break
        else:
            print("Invalid Choice")

main()