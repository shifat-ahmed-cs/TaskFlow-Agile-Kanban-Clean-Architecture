"""
Demonstration of TaskFlow: Clean Architecture, Repository Pattern, and Kanban Lifecycle.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.repositories import TaskRepository
from src.use_cases import TaskService

def main():
    print("=" * 65)
    print("      TASKFLOW: CLEAN ARCHITECTURE & ENTERPRISE DESIGN       ")
    print("=" * 65)

    repo = TaskRepository()
    service = TaskService(repo)

    # 1. Create Tasks through Application Service Layer
    t1 = service.create_task("Design Database Schema", "Create 3NF normalized tables for billing")
    t2 = service.create_task("Implement OAuth2 JWT", "Authenticate users via asymmetric RSA tokens")
    t3 = service.create_task("Deploy Kubernetes Pods", "Deploy cluster with horizontal auto-scaler")

    print("[+] Created Domain Tasks:")
    print(f"    - Task {t1['id']}: {t1['title']} [{t1['status']}]")
    print(f"    - Task {t2['id']}: {t2['title']} [{t2['status']}]")
    print(f"    - Task {t3['id']}: {t3['title']} [{t3['status']}]")

    # 2. Advance Task Lifecycle
    service.progress_task(t1["id"])  # BACKLOG -> IN_PROGRESS
    service.progress_task(t1["id"])  # IN_PROGRESS -> IN_REVIEW
    service.progress_task(t1["id"])  # IN_REVIEW -> DONE

    service.progress_task(t2["id"])  # BACKLOG -> IN_PROGRESS

    # 3. Kanban Board Distribution Metrics
    summary = service.get_kanban_summary()
    print(f"\n[+] Kanban Board Workflow Status:")
    for status, count in summary.items():
        print(f"    - {status:<15} : {count} task(s)")
    print("=" * 65)

if __name__ == "__main__":
    main()
