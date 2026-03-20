class Task:
    def __init__(self, task_id, title, description, completed=False):
        # Ensure ID is an integer for consistent comparisons
        self.id = int(task_id)
        self.title = title
        self.description = description
        self.completed = bool(completed)

    @property
    def status(self):
        return "completed" if self.completed else "pending"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }