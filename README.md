# The Codex – Python Import Mysteries

## Overview
This project explores Python import mechanics through a structured package called `alchemy`.  
It focuses on module resolution, package initialization, and dependency design.

Key topics:
- Package structure using `__init__.py`
- Absolute and relative imports
- Nested module imports
- Circular dependencies

---

## Requirements
- Python 3.10+
- Flake8 compliant code
- MyPy type annotations required
- Only project and standard library imports allowed
- No modification of `sys.path`

---

## Parts

### Alembic
Basic import usage:
- import module
- from module import function
- absolute imports

### Distillation
Package exposure:
- `__init__.py` exports
- aliases (e.g. heal)
- nested imports

### Transmutation
Import paths:
- absolute imports
- relative imports
- package-level imports

### Kaboom
Circular dependencies:
- intentional import loops
- import-time failure
- dependency resolution issues

---

## Goal
Understand how Python resolves imports and how package structure affects module visibility and dependency flow.