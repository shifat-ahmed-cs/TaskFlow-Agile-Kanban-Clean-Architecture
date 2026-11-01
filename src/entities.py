"""
Domain Entities and Invariants adhering to Clean Architecture.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class TaskStatus(Enum):
    BACKLOG = "BACKLOG"
    IN_PROGRESS = "IN_PROGRESS"
    IN_REVIEW = "IN_REVIEW"
    DONE = "DONE"

class TaskPriority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

@dataclass
class Task:
    id: int
    title: str
    description: str
    assignee_id: Optional[int] = None
    status: TaskStatus = TaskStatus.BACKLOG
    priority: TaskPriority = TaskPriority.MEDIUM

    def advance_status(self) -> None:
        transitions = {
            TaskStatus.BACKLOG: TaskStatus.IN_PROGRESS,
            TaskStatus.IN_PROGRESS: TaskStatus.IN_REVIEW,
            TaskStatus.IN_REVIEW: TaskStatus.DONE,
            TaskStatus.DONE: TaskStatus.DONE
        }
        self.status = transitions[self.status]
