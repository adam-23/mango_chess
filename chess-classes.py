"""File that holds the player and piece classes."""


class Piece:
    """Generic piece. Can hold a place, can capture, can die."""

    # def __init__(self):
    # starting location x
    # starting y
    x_loc = 0
    y_loc = 0
    team_color = ""
    is_active = True
    symbol = "*"
    available_moves = []

    def move(self):
        """How each piece moves."""
        # move protocol for piece, like move up for pawns or diag for bishes\
        # this is an example of the pawns:
        if self.team_color == "Black":
            self.y_loc -= 1
        if self.team_color == "White":
            self.y_loc += 1

    def get_moves(self, piece_list):
        """Generate available moves."""
        # TODO when moves are obtained, put them in a list and run input move.

    def team_check(self):
        """Check if piece is the same team."""
        # if team member is the same piece type, halt further movement,
        # cannot kill piece

    @staticmethod
    def capture(target):
        """Move piece to graveyard, render innert."""
        target.x_loc = 0
        target.y_loc = 0
        target.is_active = False
        # Remove all possible moves for this piece.
        # only do it if the target piece is of the different team

    # def check_loc(self):
    # Is this needed

    def compare_loc(self, target):
        """If piece is in the same spot you move to, capture it."""
        if target.x_loc == self.x_loc and target.y_loc == self.y_loc:
            self.capture(target)


class Player:
    """Class that handles all player input and if in check or not."""

    # Runs check
    # Inputs moves
    # Chooses things
    can_castle = False
    in_check = False

    def check_if_in_check(self):
        """Run protocols to determine if player in check or no."""
        # how in hell do I do this
        # check if king is in range of knight
        # use individual piece things to check if in range
        # so if I were to try a move, run it against all other piece ranges.
        # example, run pawn_check, knight_check, etc.

    def input_move(self):
        """Ask user for move."""
        # Ask user for move

    def compare_move_input(self):
        """Check if input move is in available moves list."""
        # if input move in get_moves:
        self.move()
        # MAKE THIS WORK WITH ALGEBRAIC NOTATION, and tell a piece to move.

# class Team