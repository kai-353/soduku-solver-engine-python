from board import Board


class Ops:
    """Utility operations for Sudoku boards."""
    
    @staticmethod
    def copy(board: Board) -> Board:
        """
        Create a deep copy of the board.
        
        Args:
            board: The board to copy
            
        Returns:
            A new Board with the same values
        """
        copy = Board()
        for r in range(9):
            for c in range(9):
                copy.set_value(r, c, board.get_value(r, c))
        return copy
    
    @staticmethod
    def print_board(board: Board) -> None:
        """
        Print the board to the console.
        
        Args:
            board: The board to print
        """
        for r in range(9):
            for c in range(9):
                print(board.get_value(r, c), end=" ")
            print()
        print()
