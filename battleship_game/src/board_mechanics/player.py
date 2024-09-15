from .piece import Piece
from typing import List
from .board import Board

# The pieces each player starts with in the game
STARTING_PIECES: List[Piece] = [
    Piece([[True, True, True, True, True]]),
    Piece([[True, True, True, True]]),
    Piece([[True, True, True]]),
    Piece([[True, True]]),
    Piece([[True]]),
]

# A player in the battleship game
class Player:
    # Create a new player with the given name and number of ships
    # The player will start with numberOfShips starting pieces taken from the smallest pieces in STARTING_PIECES
    def __init__(self, name: str, numberOfShips: int) -> None:
        self.name = name
        # Take numberOfShips elements from the end of STARTING_PIECES
        # These will be the smallest pieces in the list
        self.unplacedPieces = STARTING_PIECES[len(STARTING_PIECES) - numberOfShips:]
        self.board = Board()

    # Take the smallest piece (out of 5 long pieces) and return it
    # or None if all pieces have been taken
    def takeSmallestPiece(self) -> Piece | None:
        if not self.unplacedPieces:
            return None  # Return None if there are no pieces left
        return self.unplacedPieces.pop()
    
    # Get the player's name
    def getName(self) -> str:
        return self.name
    
    # Display the player
    def __str__(self) -> str:
        return self.name
