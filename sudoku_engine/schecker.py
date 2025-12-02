# This class is completely unnecessary because the solver returns True or False too,
# but it can be useful for checking if a board has a solution without modifying the original.

from board import Board
from solver import Solver
from ops import Ops


class SChecker:
    """Checks if a Sudoku board has a solution."""
    
    def __init__(self):
        """Initialize the solution checker with a solver."""
        self.solver = Solver()
    
    def has_solution(self, board: Board) -> bool:
        """
        Check if the board has a solution without modifying the original board.
        
        Args:
            board: The board to check
            
        Returns:
            True if the board has a solution, False otherwise
        """
        copy = Ops.copy(board)
        return self.solver.solve(copy)
