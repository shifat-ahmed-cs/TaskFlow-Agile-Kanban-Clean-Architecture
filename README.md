# TaskFlow: Clean Architecture RESTful Engine & Enterprise Engineering Framework

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Architecture: Clean](https://img.shields.io/badge/architecture-Clean%20Hexagonal-blue.svg)]()
[![Academic: BRACU CSE470](https://img.shields.io/badge/course-CSE%20470-orange.svg)]()

## 📌 Course Context: CSE 470 (Software Engineering)
*Department of Computer Science and Engineering, BRAC University*  
**Core Principles:** Clean Architecture / Hexagonal Architecture, Domain-Driven Design (DDD), SOLID Principles, Repository Pattern, and Agile Kanban Workflow State Transitions.

---

## 🎯 Architecture Layers

```
+-----------------------------------------------------------+
| Presentation Layer / CLI / REST API Controller            |
|                            v                              |
| Use Cases & Application Services (TaskService)             |
|                            v                              |
| Domain Entities & Business Rules (Task, TaskStatus)        |
|                            ^                              |
| Persistence & Repositories (TaskRepository Abstraction)   |
+-----------------------------------------------------------+
```

1. **Domain Layer:** Pure Python entities with state machine transitions (`BACKLOG` $\to$ `IN_PROGRESS` $\to$ `IN_REVIEW` $\to$ `DONE`).
2. **Repository Layer:** Abstract data access decoupled from concrete storage engines.
3. **Application Services:** Orchestrates business transactions and maintains audit integrity.

---

## 🚀 Quickstart & Testing
```bash
# Run demonstration
python main.py

# Run unit tests
python -m unittest discover -s tests
```
