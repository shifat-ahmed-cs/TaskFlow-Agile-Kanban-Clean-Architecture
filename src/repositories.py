"""
Repository Pattern for Abstraction of Data Persistence.
"""
from typing import Dict, List, Optional
from .entities import Task

class TaskRepository:
    def __init__(self):
        self._storage: Dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str, description: str, priority=None) -> Task:
        t_id = self._next_id
        self._next_id += 1
        task = Task(id=t_id, title=title, description=description)
        if priority:
            task.priority = priority
        self._storage[t_id] = task
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self._storage.get(task_id)

    def list_all(self) -> List[Task]:
        return list(self._storage.values())
