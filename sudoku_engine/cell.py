class Cell:
    """Represents a single cell in the Sudoku board."""
    
    def __init__(self, row: int, col: int):
        """
        Initialize a cell with its position.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
        """
        self.row = row
        self.col = col
        self.value = 0
    
    def get_row(self) -> int:
        """Get the row index of this cell."""
        return self.row
    
    def get_col(self) -> int:
        """Get the column index of this cell."""
        return self.col
    
    def get_value(self) -> int:
        """Get the value of this cell (0 if empty)."""
        return self.value
    
    def set_value(self, value: int) -> None:
        """Set the value of this cell."""
        self.value = value
    
    def is_empty(self) -> bool:
        """Check if this cell is empty."""
        return self.value == 0
