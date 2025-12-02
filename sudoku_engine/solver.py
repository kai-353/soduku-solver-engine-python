from board import Board
from validator import Validator


class Solver:
    """Solves Sudoku puzzles using backtracking algorithm."""
    
    def solve(self, board: Board) -> bool:
        """
        Solve the Sudoku puzzle using backtracking.
        
        Args:
            board: The Sudoku board to solve
            
        Returns:
            True if the puzzle is solved, False if no solution exists
        """
        for r in range(9):
            for c in range(9):
                if board.is_empty(r, c):
                    for num in range(1, 10):
                        if Validator.is_valid(board, r, c, num):
                            board.set_value(r, c, num)
                            
                            if self.solve(board):
                                return True
                            
                            board.set_value(r, c, 0)
                    
                    return False
        
        return True
