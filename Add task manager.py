tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "✔" if task["done"] else "❌"
            print(f"{i + 1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def delete_task():
    show_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted!")
    else:
        print("Invalid index")

def mark_done():
    show_tasks()
    index = int(input("Enter task number to mark done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Task completed!")
    else:
        print("Invalid index")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Mark Done\n5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
