"""
Application Business Rules (Use Cases).
"""
from typing import List, Dict, Any
from .repositories import TaskRepository
from .entities import TaskStatus

class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, title: str, desc: str) -> Dict[str, Any]:
        task = self.repo.add(title, desc)
        return {"id": task.id, "title": task.title, "status": task.status.value}

    def progress_task(self, task_id: int) -> Dict[str, Any]:
        task = self.repo.get_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        task.advance_status()
        return {"id": task.id, "title": task.title, "new_status": task.status.value}

    def get_kanban_summary(self) -> Dict[str, int]:
        tasks = self.repo.list_all()
        summary = {status.value: 0 for status in TaskStatus}
        for t in tasks:
            summary[t.status.value] += 1
        return summary
