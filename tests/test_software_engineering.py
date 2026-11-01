"""
Unit tests for TaskFlow Clean Architecture services.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.repositories import TaskRepository
from src.use_cases import TaskService
from src.entities import TaskStatus

class TestTaskFlow(unittest.TestCase):
    def test_task_lifecycle(self):
        repo = TaskRepository()
        svc = TaskService(repo)
        t = svc.create_task("Test Task", "Desc")
        self.assertEqual(t["status"], TaskStatus.BACKLOG.value)

        p = svc.progress_task(t["id"])
        self.assertEqual(p["new_status"], TaskStatus.IN_PROGRESS.value)

if __name__ == "__main__":
    unittest.main()
