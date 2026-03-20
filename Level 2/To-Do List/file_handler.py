# Handle CSV Operation

import csv
import os

from tasks import Task


class FileHandler:
    def __init__(self, file):
        self.file = file

    def read_tasks(self):
        tasks = []
        if os.path.exists(self.file):
            with open(self.file, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    completed = str(row.get("status", "")).strip().lower() == "completed"
                    tasks.append(
                        Task(
                            row.get("id", "0"),
                            row.get("title", ""),
                            row.get("description", ""),
                            completed=completed,
                        )
                    )
        return tasks

    def write_tasks(self, tasks):
        with open(self.file, mode='w', newline='') as csvfile:
            fieldnames = ["id", "title", "description", "status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                if isinstance(task, Task):
                    row = task.to_dict()
                elif isinstance(task, dict):
                    row = task
                else:
                    # Fall back to converting using __dict__, if available
                    row = getattr(task, "__dict__", {})
                writer.writerow(row)
