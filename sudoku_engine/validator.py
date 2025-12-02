from board import Board


class Validator:
    """Validates Sudoku board moves."""
    
    @staticmethod
    def is_valid(board: Board, row: int, col: int, num: int) -> bool:
        """
        Check if placing a number at the specified position is valid.
        
        Args:
            board: The Sudoku board
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)
            
        Returns:
            True if the placement is valid, False otherwise
        """
        # Check row and column
        for i in range(9):
            if board.get_value(row, i) == num or board.get_value(i, col) == num:
                return False
        
        # Check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board.get_value(r, c) == num:
                    return False
        
        return True
