try:
    from .cell import Cell
except ImportError:
    from cell import Cell


class Board:
    """Represents a 9x9 Sudoku board."""

    def __init__(self):
        """Initialize a 9x9 board with empty cells."""
        self.cells = [[Cell(r, c) for c in range(9)] for r in range(9)]

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Get the cell at the specified position.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)

        Returns:
            The Cell object at the specified position
        """
        return self.cells[row][col]

    def get_value(self, row: int, col: int) -> int:
        """
        Get the value at the specified position.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)

        Returns:
            The value at the specified position (0 if empty)
        """
        return self.cells[row][col].get_value()

    def set_value(self, row: int, col: int, val: int) -> None:
        """
        Set the value at the specified position.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            val: Value to set (0-9, where 0 means empty)
        """
        self.cells[row][col].set_value(val)

    def is_empty(self, row: int, col: int) -> bool:
        """
        Check if the cell at the specified position is empty.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)

        Returns:
            True if the cell is empty, False otherwise
        """
        return self.cells[row][col].is_empty()
