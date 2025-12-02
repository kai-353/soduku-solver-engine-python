# Python Sudoku Solver Engine

A Python implementation of a Sudoku solver using a backtracking algorithm. This is a port of the Java sudoku-solver-engine by konraaadcz.

## Structure

- `cell.py` - Represents a single cell in the Sudoku board
- `board.py` - Represents the 9x9 Sudoku board
- `validator.py` - Validates Sudoku moves according to the rules
- `solver.py` - Solves Sudoku puzzles using backtracking
- `move.py` - Represents a single move on the board
- `history.py` - Manages the history of moves
- `ops.py` - Utility operations (copy, print)
- `schecker.py` - Checks if a board has a solution without modifying it
- `example.py` - Example usage of the solver

## Installation

### Install Locally

To install this package locally for development or personal use:

```bash
# Clone the repository
git clone https://github.com/kai-353/sudoku-solver-engine-python.git
cd sudoku-solver-engine-python

# Install with pip/pip3
pip install -e .
```

After installation, you can import and use the package from anywhere:

```python
from sudoku_engine import Board, Solver, Ops
```

## Usage

### Basic Example

```python
from sudoku_engine import Board, Solver, Ops

# Create a new board
board = Board()

# Set up your puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Load the puzzle
for r in range(9):
    for c in range(9):
        board.set_value(r, c, puzzle[r][c])

# Solve it
solver = Solver()
if solver.solve(board):
    print("Solved!")
    Ops.print_board(board)
else:
    print("No solution exists!")
```

### Running the Example

```bash
python -m sudoku_engine.example
```

## Features

- **Backtracking Algorithm**: Efficient solving using recursive backtracking
- **Validation**: Checks row, column, and 3x3 box constraints
- **Board Operations**: Copy and print utilities
- **Move History**: Track changes made to the board
- **Solution Checking**: Verify if a puzzle has a solution without modifying the original

## API

### Board

- `Board()` - Create a new empty board
- `get_value(row, col)` - Get the value at position (row, col)
- `set_value(row, col, val)` - Set the value at position (row, col)
- `is_empty(row, col)` - Check if position (row, col) is empty

### Solver

- `solve(board)` - Solve the board in-place, returns True if solvable

### Validator

- `Validator.is_valid(board, row, col, num)` - Check if placing num at (row, col) is valid

### Ops

- `Ops.copy(board)` - Create a deep copy of the board
- `Ops.print_board(board)` - Print the board to console

### SChecker

- `has_solution(board)` - Check if board has a solution without modifying it

## Requirements

- Python 3.6+

No external dependencies required.

## Credits

The sudoku engine code is based on the java version made by konraaadcz (https://github.com/konraaadcz/sudoku-solver-engine)
