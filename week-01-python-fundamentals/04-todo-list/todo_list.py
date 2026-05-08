import json
import os

tasks_file = "tasks.json"

def load_tasks():
    #if tasks_file doesn't exist, return an empty list

    #otherwise, open it and return json.load(f)
    pass

def save_tasks():
    # open tasks_file for writing, json.dump(tasks, f, indent = 2)
    pass

def add_task(tasks):
    text = input("Task description: ").strip()
    # calculate next id (max existing id +1, or 1 if empty)
    # Append a new task dict {"id": ..., "text": ..., "done": false}
    pass

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet")
        return
    
    #Loop through tasks, print each as:
    # "[] 1. Buy groceries" for not-done
    # "[x] 2. call num" for done

def mark_complete(tasks):
    #show list, ask for id, set that task's done to true
    pass

def delete_task(tasks):

    # show list, ask for id, remove that task from list
    pass

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
            list_tasks()
        elif choice == "3":
            mark_complete(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Good Bye.")
            break
        else:
            print("Invalid Choice")

main()