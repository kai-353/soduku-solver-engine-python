from move import Move


class History:
    """Manages the history of moves on the board."""
    
    def __init__(self):
        """Initialize an empty move history."""
        self.moves = []
    
    def push(self, move: Move) -> None:
        """
        Add a move to the history.
        
        Args:
            move: The move to add
        """
        self.moves.append(move)
    
    def pop(self) -> Move:
        """
        Remove and return the most recent move.
        
        Returns:
            The most recent move, or None if history is empty
        """
        if self.is_empty():
            return None
        return self.moves.pop()
    
    def is_empty(self) -> bool:
        """
        Check if the history is empty.
        
        Returns:
            True if history is empty, False otherwise
        """
        return len(self.moves) == 0
