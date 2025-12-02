class Move:
    """Represents a move on the Sudoku board."""
    
    def __init__(self, row: int, col: int, previous_value: int, new_value: int):
        """
        Initialize a move.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            previous_value: The value before the move
            new_value: The value after the move
        """
        self.row = row
        self.col = col
        self.previous_value = previous_value
        self.new_value = new_value
    
    def get_row(self) -> int:
        """Get the row index of this move."""
        return self.row
    
    def get_col(self) -> int:
        """Get the column index of this move."""
        return self.col
    
    def get_previous_value(self) -> int:
        """Get the previous value before this move."""
        return self.previous_value
    
    def get_new_value(self) -> int:
        """Get the new value after this move."""
        return self.new_value
