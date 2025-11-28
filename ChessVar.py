# Author: Jeffrey Maher
# GitHub username: maherje
# Date: 5/26/2024
# Description: Portfolio Project. Create an Atomic Chess game; a variant of the game Chess.


class Piece:
    """
    A class for creating chess game piece objects. Subclassed by the Rook, Knight, Bishop, Queen, King and Pawn
    classes. Holds data about the piece's color and symbol representation.

    DATA MEMBERS
    ------------
    _color: str
        The color of the piece. White or Black.
    _symbol: str
        The symbol representation of the piece. Will be shown when the board state is printed out.
    _move_directions: list[(int, int)]
        Allowable move directions for the piece defined as a list of (row, col) movement tuples.
    _max_movement: int
        The maximum number of spaces the piece can move in any of the directions defined in _move_directions.

    METHODS
    -------
    __init__(color: str) -> None
        Initialize a chess piece object or a certain color (white or black). Set initial values for symbol,
        move_directions and max_movement.
    get_symbol() -> str
        Returns the piece object's symbol.
    get_color() -> str
        Returns the piece object's color.
    get_move_directions -> list[tuple[int, int]]
        Returns the piece objects move directions list.
    get_max_movement -> int
        Returns the piece objects max movement.
    """

    def __init__(self, color: str) -> None:
        self._color = color
        self._symbol = ""
        self._move_directions = [(0, 0)]
        self._max_movement = 0

    def get_symbol(self) -> str:
        """ Returns the piece's symbol """
        return self._symbol

    def get_color(self) -> str:
        """ Returns the piece's color """
        return self._color

    def get_move_directions(self) -> list[tuple[int, int]]:
        """ Returns the piece's move_directions list """
        return self._move_directions

    def get_max_movement(self) -> int:
        """ Returns the piece's max movement """
        return self._max_movement


class Rook(Piece):
    """
    A class for Rook objects. Inherits from the Piece class. Includes information about how the Rook piece can move
    in addition to its name, color and symbol data. See Piece class for documentation on data members and methods.
    """

    def __init__(self, color: str):
        super().__init__(color)
        # The Rook moves up or down on orthogonal directions.
        self._max_movement = 7
        self._move_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if self._color == "white":  # ♖
            self._symbol = "r"
        else:  # ♜
            self._symbol = "R"


class Knight(Piece):
    """
    A class for Knight objects. Inherits from the Piece class. Includes information about how the Knight piece can
    move in addition to its name, color and symbol data. See Piece class for documentation on data members and methods.
    """

    def __init__(self, color: str):
        super().__init__(color)
        # The Knight moves 2 squares in one orthogonal direction and then 1 in the other orthogonal direction.
        # The Knight can jump other pieces.
        self._max_movement = 1
        self._move_directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        if self._color == "white":  # ♘
            self._symbol = "n"
        else:  # ♞
            self._symbol = "N"


class Bishop(Piece):
    """
    A class for Bishop objects. Inherits from the Piece class. Includes information about how the Bishop piece can
    move in addition to its name, color and symbol data. See Piece class for documentation on data members and methods.
    """

    def __init__(self, color: str):
        super().__init__(color)
        # Bishop moves up or down on the diagonal.
        self._max_movement = 7
        self._move_directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        if self._color == "white":  # ♗
            self._symbol = "b"
        else:  # ♝
            self._symbol = "B"


class Queen(Piece):
    """
    A class for Queen objects. Inherits from the Piece class. Includes information about how the Queen piece can
    move in addition to its name, color and symbol data. See Piece class for documentation on data members and methods.
    """

    def __init__(self, color: str):
        super().__init__(color)
        # The Queen can move in any orthogonal or diagonal direction.
        self._max_movement = 7
        self._move_directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        if self._color == "white":  # ♕
            self._symbol = "q"
        else:  # ♛
            self._symbol = "Q"


class King(Piece):
    """
    A class for King objects. Inherits from the Piece class. Includes information about how the King piece can
    move in addition to its name, color and symbol data. See Piece class for documentation on data members and methods.
    """

    def __init__(self, color: str):
        super().__init__(color)
        # The King can move one square in any orthogonal or diagonal direction.
        self._max_movement = 1
        self._move_directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        if self._color == "white":  # ♔
            self._symbol = "k"
        else:  # ♚
            self._symbol = "K"


class Pawn(Piece):
    """
    A class for Pawn objects. Inherits from the Piece class. Includes information about how the Pawn piece can
    move (white and black pawns move slightly differently) and capture in addition to its name, color and symbol data.
    See Piece class for documentation on data members and methods. Data members and methods unique to Pawn class listed
    below.

    DATA MEMBERS
    ------------
    _capture_directions: list[tuple[int, int]]
        Allowable capture directions for the pawn defined as a list of (row, col) movement tuples.

    METHODS
    -------
    get_capture_directions -> list[tuple[int, int]]:
        Returns the piece objects capture directions list.
    set_max_movement(num: int) -> None:
        Set the _max_movement data member to a new value.
    """

    def __init__(self, color: str):
        super().__init__(color)
        # Pawns can move 2 spaces on their first movement.
        self._max_movement = 2
        if self._color == "white":  # ♙
            # White pawns can only move up.
            self._move_directions = [(1, 0)]
            # White pawns capture on the up diagonals.
            self._capture_directions = [(1, 1), (1, -1)]
            self._symbol = "p"
        else:  # ♟
            # Black pawns can only move down.
            self._move_directions = [(-1, 0)]
            # Black pawns capture on the down diagonals.
            self._capture_directions = [(-1, 1), (-1, -1)]
            self._symbol = "P"

    def get_capture_directions(self) -> list[tuple[int, int]]:
        """ Returns the capture directions """
        return self._capture_directions

    def set_max_movement(self, num: int) -> None:
        """
        Set the max number of per turn movements for the pawn. Meant to be used to reduce pawn space movement
        from two to one after the pawns first move of the game.
        """
        self._max_movement = num


class ChessVar:
    """
    An object for an Atomic Chess game. Initializes a chess board with pieces in their default starting positions.
    Provides methods for querying pieces currently on the board, setting and getting pieces on the board, getting the
    current board state, determining current turn, printing the board state, moving pieces around the board,
    determining legal moves for a particular piece on the board and, handling explosion actions.

    DATA MEMBERS
    ------------
    _is_white_turn: bool
        Turn tracking variable. White's turn when True, Black's turn when False.
    _col_name_conv: dict[str, int]
        A dictionary for converting the chess board column names between alpha values and int values.
    _board: list[list[None | str | Piece]]
        A list of lists that represents the squares on the chess board. Most entries will either be None (empty square)
        or a Piece object. Edge entries could be strings representing row and column names.

    METHODS
    -------
    __init__
        A method for creating a ChessVar object. Initializes the board data member with pieces in their starting
        positions and sets the turn to the white player.
    get_board -> list[list[str | None | Piece]]
        Returns the chess board data member.
    clear_board -> None
        Clears the chess board of all pieces.
    get_kings_on_board(piece) -> list[Piece]
        Returns a list of all Kings currently on the board.
    set_piece_at_square(square: str, piece: Piece | None) -> None
        Takes a square location in algebraic notation and a Piece object and places the Piece object at that location.
    get_piece_at_square(square: str) -> piece: Piece | None
        Takes the algebraic notation for a square and returns the Piece object at that square.
    get_game_state -> str
        Determines and returns the current state of the game which is either "WHITE_WON", "BLACK_WON" or "UNFINISHED"
    whose_turn -> str
        Returns a string ("white" or "black") representing the current player's turn.
    switch_turn -> None
        Changes the current player to the other player.
    print_board -> None
        Prints the current board state to the console.
    legal_pawn_moves(square) -> list[str]
        Take a chess pawn and return a list of legal squares they can move to or capture at based on the current board
        state.
    legal_moves(square) -> list[str]
        Take a chess square and return a list of legal squares they can move to based on the current board state.
    is_valid_explosion(capturing_piece, square) -> bool
        Take a capturing piece, and a square and validate an explosion at the square. Return True if the explosion is
        legal and False otherwise.
    explode(square) -> None
        Take a square and execute an explode action by updating appropriate squares and player pieces.
    make_move(start, end) -> bool
        Takes a start and end location and attempts to move the chess piece at the start location to the end location.
        Returns True for a successful move and False for an unsuccessful move.
    """

    def __init__(self):
        """Initialize a new chess board with pieces in their proper locations and stored in a board data member which is
        a list of lists. Start the first game turn with the white player. """

        self._is_white_turn: bool = True  # White has the first turn.
        # Create a conversion dict for converting between column alpha value and number index for the board data member.
        self._col_name_conv: dict[str | int, str | int] = \
            {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
             1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

        rows = range(1, 9)  # Eight number named rows in a chess board
        cols = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # Eight alpha named columns in a chess board.

        # Create the first row of a blank board.
        self._board: list[list[None | str | Piece]] = [[None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
        # Create the rest of the blank board.
        for row in rows:
            self._board.append([row] + [None] * 8)

        # Create the starting pieces.
        white_pieces = [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"),
                        Knight("white"), Rook("white")]

        white_pawns = [Pawn('white') for _ in range(8)]

        black_pieces = [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"),
                        Knight("black"), Rook("black")]

        black_pawns = [Pawn('black') for _ in range(8)]

        # Put all the chess pieces into an iterable object.
        game_pieces = (white_pieces, white_pawns, black_pawns, black_pieces)

        # Put the pieces on the board in their proper squares.
        for row, piece in zip((1, 2, 7, 8), range(len(game_pieces))):
            for col, index in zip(cols, range(8)):
                self.set_piece_at_square(col + str(row), game_pieces[piece][index])

    def get_board(self) -> list[list[str | None | Piece]]:
        """ Returns the chess board data member."""
        return self._board

    def clear_board(self) -> None:
        """ Clear the chess board of all pieces. For creating test cases."""

        for row in range(9):
            for col in range(9):
                if isinstance(self._board[row][col], Piece):
                    self._board[row][col] = None

    def get_kings_on_board(self) -> list[King]:
        """
        Returns a list of all Kings currently on the board.
        """

        active_pieces = []

        for row in self._board:
            for col in row:
                if isinstance(col, King):
                    active_pieces.append(col)

        return active_pieces

    def set_piece_at_square(self, square: str, piece: Piece | None) -> None:
        """
        Takes a square location in algebraic notation and a Piece object and places the Piece object at that location.
        """

        col = self._col_name_conv[square[0]]
        row = int(square[1])

        self._board[row][col] = piece

    def get_piece_at_square(self, square: str) -> King | Queen | Rook | Bishop | Knight | Pawn | None:
        """
        Takes the algebraic notation for a square and returns the Piece object at that square.
        """

        col = self._col_name_conv[square[0]]
        row = int(square[1])

        return self._board[row][col]

    def get_game_state(self) -> str:
        """
        Determines and returns the current state of the game which is either "WHITE_WON", "BLACK_WON" or "UNFINISHED"
        """
        kings_list = self.get_kings_on_board()
        if len(kings_list) == 2:
            return "UNFINISHED"  # Both kings are still on the board. Game has not finished.

        # There must only be one king left on the board. Check it's color.
        if kings_list[0].get_color() == "white":
            return "WHITE_WON"
        else:
            return "BLACK_WON"

    def whose_turn(self) -> str:
        """ Returns a string ("white" or "black") representing the current player's turn. """

        if self._is_white_turn:
            return "white"
        else:
            return "black"

    def switch_turn(self) -> None:
        """ Changes the current player to the other player. """

        if self._is_white_turn:
            self._is_white_turn = False
        else:
            self._is_white_turn = True

    def print_board(self) -> None:
        """ Prints the current board state to the console. """
        for row in self._board[::-1]:
            for col in row:
                if isinstance(col, Piece):  # Is the item a chess piece?
                    print(f'{col.get_symbol()}', end=' ')
                elif col is None:
                    print(f'·', end=' ')
                else:
                    print(f'{col}|', end='')

            print()

    def legal_pawn_moves(self, square: str) -> list[str]:
        """
        Take a chess pawn and return a list of legal squares they can move to or capture at based on the current board
        state.
        """

        piece = self.get_piece_at_square(square)
        piece_color = piece.get_color()
        legal_move_list = []
        moves = piece.get_move_directions()
        max_movement = piece.get_max_movement()
        captures = piece.get_capture_directions()

        for move in moves:
            num_moves = 0
            starting_col, starting_row = self._col_name_conv[square[0]], int(square[1])
            while num_moves < max_movement:
                new_col, new_row = starting_col + move[1], starting_row + move[0]
                if 0 < new_col < 9 and 0 < new_row < 9:
                    new_square = self._board[new_row][new_col]
                    if new_square is None:
                        legal_move_list.append(str(self._col_name_conv[new_col]) + str(new_row))
                        starting_col, starting_row = new_col, new_row
                        num_moves += 1
                    else:
                        break

        for capture in captures:
            starting_col, starting_row = self._col_name_conv[square[0]], int(square[1])
            new_col, new_row = starting_col + capture[1], starting_row + capture[0]
            if 0 < new_col < 9 and 0 < new_row < 9:
                new_square = self._board[new_row][new_col]
                if new_square is not None and new_square.get_color() != piece_color:
                    legal_move_list.append(str(self._col_name_conv[new_col]) + str(new_row))

        return legal_move_list

    def legal_moves(self, square: str) -> list[str]:
        """
        Take a chess square and return a list of legal squares they can move to based on the current board state.
        """

        piece = self.get_piece_at_square(square)
        piece_color = piece.get_color()
        legal_move_list = []
        moves = piece.get_move_directions()
        max_movement = piece.get_max_movement()

        try:
            for move in moves:
                num_moves = 0
                starting_col, starting_row = self._col_name_conv[square[0]], int(square[1])
                while num_moves < max_movement:
                    new_col, new_row = starting_col + move[1], starting_row + move[0]
                    if new_col > 8 or new_col < 1 or new_row > 8 or new_row < 1:  # Piece cannot move off the board.
                        break
                    new_square = self._board[new_row][new_col]
                    if new_square is None:  # Square is open.
                        legal_move_list.append(str(self._col_name_conv[new_col]) + str(new_row))
                        starting_col, starting_row = new_col, new_row
                        num_moves += 1
                    elif new_square.get_color() == piece_color:  # Square contains another of the player's pieces.
                        break
                    elif isinstance(piece, King):  # A king cannot capture.
                        break
                    else:  # Square contains the opponent's piece. Move is legal; stop further movement.
                        legal_move_list.append(str(self._col_name_conv[new_col]) + str(new_row))
                        break
        except IndexError:
            print(f'Index error: legal_moves, move at square: {square}')
            self.print_board()

        return legal_move_list

    def is_valid_explosion(self, capturing_piece: Piece, square: str) -> bool:
        """
        Take a capturing piece, and a square and validate an explosion at the square. Return True if the explosion is
        legal and False otherwise.
        """

        pieces_in_blast_zone = []
        col_index, row_index = self._col_name_conv[square[0]], int(square[1])

        try:
            for col in range(col_index - 1, col_index + 2):
                for row in range(row_index - 1, row_index + 2):
                    if 0 < col < 9 and 0 < row < 9:  # Stay on the board.
                        piece = self.get_piece_at_square(self._col_name_conv[col] + str(row))
                        if piece is not None:
                            pieces_in_blast_zone.append(piece)
            if capturing_piece not in pieces_in_blast_zone:
                pieces_in_blast_zone.append(capturing_piece)

            num_kings = 0
            for piece in pieces_in_blast_zone:
                if isinstance(piece, King):
                    num_kings += 1
            if num_kings == 2:
                return False
            else:
                return True
        except IndexError:
            print(f'Index error: is_valid_explosion, at square: {square} with piece: {capturing_piece.get_symbol()}')
            self.print_board()

    def explode(self, square: str) -> None:
        """
        Take a square and execute an explode action by updating appropriate squares and player pieces.
        """

        col_index, row_index = self._col_name_conv[square[0]], int(square[1])
        for col in range(col_index - 1, col_index + 2):
            for row in range(row_index - 1, row_index + 2):
                if 0 < col < 9 and 0 < row < 9:  # Stay on the board.
                    piece = self.get_piece_at_square(self._col_name_conv[col] + str(row))
                    if piece is not None and not (isinstance(piece, Pawn)):
                        self.set_piece_at_square(self._col_name_conv[col] + str(row), None)

    def make_move(self, start: str, end: str) -> bool:
        """
        Takes a start and end location and attempts to move the chess piece at the start location to the end location.
        Returns True for a successful move and False for an unsuccessful move.
        """
        # Check that start and end squares are legitimate.
        if start[0] not in self._col_name_conv or end[0] not in self._col_name_conv:
            return False

        if int(start[1]) not in self._col_name_conv.values() or int(end[1]) not in self._col_name_conv.values():
            return False

        # Get the current player
        current_player = self.whose_turn()

        piece_at_start_square = self.get_piece_at_square(start)  # Piece on starting square.
        if piece_at_start_square is None:
            return False  # No valid piece to move.

        start_piece_color = piece_at_start_square.get_color()  # Color of the piece on the starting square.
        if start_piece_color != current_player:
            return False  # Illegal move. Starting piece doesn't belong to current player.

        piece_at_end_square = self.get_piece_at_square(end)  # Piece on the ending square.
        if piece_at_end_square is not None:
            end_piece_color = piece_at_end_square.get_color()  # Color of the piece on the ending square.
            if end_piece_color == current_player:
                return False  # Illegal move. End square piece belongs to the current player.

        # Is the end location accessible for the start spot piece?
        if isinstance(piece_at_start_square, Pawn):
            list_of_legal_squares = self.legal_pawn_moves(start)
        else:
            list_of_legal_squares = self.legal_moves(start)

        if end not in list_of_legal_squares:
            # Proposed move is not legal as the starting piece is unable to move to the end piece.
            return False

        if piece_at_end_square is None:
            # Execute the move. Update board state.
            if isinstance(piece_at_start_square, Pawn):
                piece_at_start_square.set_max_movement(1)
            self.set_piece_at_square(end, piece_at_start_square)
            self.set_piece_at_square(start, None)
            self.switch_turn()
            return True

        # Validate explosion.
        if self.is_valid_explosion(piece_at_start_square, end):
            if isinstance(piece_at_start_square, Pawn):
                piece_at_start_square.set_max_movement(1)
            self.set_piece_at_square(start, None)
            self.set_piece_at_square(end, None)
            # Execute explosion action
            self.explode(end)
            self.switch_turn()
            return True
        else:
            return False
