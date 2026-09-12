# CS4300 - Homework 1

## What the Project Is

This is a Python homework assignment consisting of 7 tasks that cover fundamental programming concepts:

- **Task 1**: Basic "Hello, World!" program
- **Task 2**: Working with data types (integers, floats, strings, booleans)
- **Task 3**: Control flow - conditionals, loops, and prime number generation
- **Task 4**: Arithmetic operations - calculating discounts
- **Task 5**: Data structures - lists and dictionaries
- **Task 6**: File I/O - counting words in a text file
- **Task 7**: HTTP requests - fetching status codes from web URLs

## How to Run It

Each task is a standalone Python script located in the `src/` directory. You can run individual tasks from the homework1 directory:

```bash
# Run a specific task
python src/task1.py
python src/task2.py
python src/task3.py
python src/task4.py
python src/task5.py
python src/task6.py
python src/task7.py
```

Note: Some tasks define functions that need to be imported or called (e.g., Task 2, Task 5). You can also import and use them in a Python REPL:

```python
from src.task2 import get_integer, get_float, get_string, get_boolean
from src.task5 import first_three_books, students
```

## How to Test It

This project uses `pytest` for unit testing. Tests are located in the `tests/` directory.

### Running All Tests

```bash
pytest
```

### Running Tests for a Specific Task

```bash
pytest tests/test_task1.py
pytest tests/test_task2.py
pytest tests/test_task3.py
pytest tests/test_task4.py
pytest tests/test_task5.py
pytest tests/test_task6.py
pytest tests/test_task7.py
```

### Running with Verbose Output

```bash
pytest -v
```

### Requirements

Make sure you have pytest installed:

```bash
pip install pytest
pip install requests
```

