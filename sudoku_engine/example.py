"""
Example usage of the Sudoku solver engine.
"""

try:
    from .board import Board
    from .solver import Solver
    from .ops import Ops
except ImportError:
    from board import Board
    from solver import Solver
    from ops import Ops


def main():
    # Create a new board
    board = Board()

    # Example puzzle (0 represents empty cells)
    puzzle = [
        [0, 0, 8, 0, 2, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 8, 0, 2, 0],
        [0, 4, 0, 0, 0, 6, 1, 9, 0],
        [9, 0, 0, 0, 3, 5, 0, 8, 0],
        [0, 6, 0, 0, 0, 0, 0, 5, 0],
        [0, 5, 0, 7, 6, 0, 0, 0, 9],
        [0, 2, 7, 6, 0, 0, 0, 4, 0],
        [0, 9, 0, 5, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 9, 0, 5, 0, 0],
    ]

    # Load the puzzle into the board
    for r in range(9):
        for c in range(9):
            board.set_value(r, c, puzzle[r][c])

    print("Original puzzle:")
    Ops.print_board(board)

    # Solve the puzzle
    solver = Solver()
    if solver.solve(board):
        print("Solved puzzle:")
        Ops.print_board(board)
    else:
        print("No solution exists!")


if __name__ == "__main__":
    main()
