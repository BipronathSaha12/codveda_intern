from todo import ToDoList
from file_handler import FileHandler
from tasks import Task


def main():
    todo_list = ToDoList('tasks.csv')
    todo_list.load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
            todo_list.save_tasks()
        elif choice == '2':
            task_id = int(input("Enter task ID to complete: "))
            todo_list.complete_task(task_id)
            todo_list.save_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
            todo_list.save_tasks()
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
# Run the main function
if __name__ == "__main__":
    main()