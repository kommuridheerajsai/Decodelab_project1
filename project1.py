my_tasks = []

while True:
    print("=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("Enter your choice from the list above:")
    choice  = input()
    if choice == '1':
        print("Enter the task you want to add:")
        task = input()
        my_tasks.append(task)
        print("Task added successfully!")
    elif choice == '2':
        if not my_tasks:
            print("No tasks in the list.")
        else:
            print("Your Tasks:")
            for idx, task in enumerate(my_tasks, start=1):
                print(f"{idx}. {task}")
    elif choice == '3':
        if not my_tasks:
            print("No tasks to remove.")
        else:
            print("Enter the number of the task you want to remove:")
            try:
                task_num = int(input())
                if 1 <= task_num <= len(my_tasks):
                    removed_task = my_tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
