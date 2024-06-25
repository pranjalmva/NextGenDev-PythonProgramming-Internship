todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list!")

def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def delete_task(task_number):
    try:
        del todo_list[task_number - 1]
        print(f"Task {task_number} deleted!")
    except IndexError:
        print("Invalid task number!")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
