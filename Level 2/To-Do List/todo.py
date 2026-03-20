from file_handler import FileHandler
from tasks import Task

class ToDoList:
    def __init__(self, file):
        self.file = file
        self.tasks = []

    # load tasks from file
    def load_tasks(self):
        file_handler = FileHandler(self.file)
        loaded = file_handler.read_tasks()
        # Normalize to Task objects
        self.tasks = []
        for item in loaded:
            if isinstance(item, Task):
                self.tasks.append(item)
                continue
            # Expecting dict-like rows from CSV
            task_id = item.get("id")
            title = item.get("title", "")
            description = item.get("description", "")
            status = item.get("status", "")
            completed = str(status).strip().lower() == "completed"
            self.tasks.append(Task(task_id, title, description, completed=completed))

    # save tasks to file
    def save_tasks(self):
        file_handler = FileHandler(self.file)
        file_handler.write_tasks(self.tasks)

    # add a new task
    def add_task(self, title, description):
        next_id = max((task.id for task in self.tasks), default=0) + 1
        task = Task(next_id, title, description)
        self.tasks.append(task)

    # mark a task as completed
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                break

    # delete a task
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]

    # display all tasks
    def display_tasks(self):
        for task in self.tasks:
            print(
                f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {task.status}"
            )

# Example usage 
if __name__ == "__main__":
    todo_list = ToDoList('tasks.csv')
    todo_list.load_tasks()
    todo_list.add_task("Buy groceries", "Milk, Bread, Eggs")
    todo_list.add_task("Read a book", "The Great Gatsby")
    todo_list.complete_task(1)
    todo_list.display_tasks()
    todo_list.save_tasks()
    todo_list.delete_task(2)
    todo_list.display_tasks()
    todo_list.save_tasks()
    