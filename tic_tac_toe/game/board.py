from ..resources.constants import PLAYER_2_MARK, PLAYER_1_MARK, DEFAULT_MARK


class Board:
    def __init__(self, board_size=3, board_id="", player_symbols=[], default_mark=DEFAULT_MARK, board=[]):
        self.board_size = board_size
        self.board_id = board_id
        self.player_symbols = player_symbols
        self.default_mark = default_mark
        self.board = self.initalize_board() if board == [] else board
        self._set_player_symbols()

    def _set_player_symbols(self):
        if len(self.player_symbols) == 0:
            self.player_symbols = [PLAYER_2_MARK, PLAYER_1_MARK]

    def initalize_board(self):
        row_col_size = self.board_size
        board = []
        for i in range(row_col_size):
            col = []
            for j in range(row_col_size):
                col.append(self.default_mark)
            board.append(col)
        return board

    def get_board(self):
        return self.board

    def get_board_string(self):
        board = self.board
        board_string = ''
        board_string += self.generate_row_delimeter()
        for row in range(len(board)):
            for col in range(len(board[row])):
                board_string += board[row][col]
                if col + 1 < len(board[row]):
                    board_string += '|'
                else:
                    board_string += '\n'
            board_string += self.generate_row_delimeter()
        return board_string

    def generate_row_delimeter(self):
        seed_string = '-+'
        delimeter_string = seed_string * (self.board_size - 1)
        delimeter_string += '-\n'
        return delimeter_string

    def set_cell(self, row, col, value):
        self.board[row][col] = value

    def get_cell_value(self, row, col):
        return self.board[row][col]

    def is_board_full(self):
        for row in self.board:
            for col in row:
                if not self._cell_is_set(col):
                    return False
        return True

    def _cell_is_set(self, cell):
        if cell in self.player_symbols:
            return True
        return False

    def is_cell_set(self, row, col):
        if self._cell_is_set(self.board[row][col]):
            return True
        return False
