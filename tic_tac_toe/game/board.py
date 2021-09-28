import random
from ..resources.constants import CONST_O, CONST_X, CONST_BOARD_DEFAULT_CHAR


class Board:
    def __init__(self, board_size=3, board_id="", player_symbols=[], default_board_char=None):
        self.board_size = board_size
        self.board_id = board_id
        self.player_symbols = player_symbols
        self.default_board_char = default_board_char
        self.board = []
        self._set_default_board_char()
        self._set_player_symbols()
        self.initalize_board()

    def _set_player_symbols(self):
        if len(self.player_symbols) == 0:
            self.player_symbols = [CONST_O, CONST_X]

    def _set_default_board_char(self):
        if not self.default_board_char:
            self.default_board_char = CONST_BOARD_DEFAULT_CHAR

    def initalize_board(self):
        row_col_size = self.board_size
        board = []
        for i in range(row_col_size):
            col = []
            for j in range(row_col_size):
                col.append(self.default_board_char)
            board.append(col)
        self.board = board

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

    def is_horizontal_win(self):
        for row in self.board:
            if self.list_has_wins(row):
                return row[0]
        return False

    def list_has_wins(self, input_list):
        result = input_list.count(input_list[0])

        if input_list[0] in self.player_symbols and result == len(input_list):
            return input_list[0]
        return False
