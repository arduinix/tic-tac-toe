from .cell import Cell
import random
from ..resources.constants import CONST_O, CONST_X


class Board:
    def __init__(self, board_size=3, board_id="", player_symbols=[]):
        self.board_size = board_size
        self.board_id = board_id
        self.player_symbols = player_symbols
        self.board = []
        self.initalize_board()

    def _set_player_symbols(self):
        if len(self.player_symbols) == 0:
            self.player_symbols = [CONST_O, CONST_X]

    def initalize_board(self):
        row_col_size = self.board_size
        board = []
        for i in range(row_col_size):
            col = []
            for j in range(row_col_size):
                col.append(Cell())
            board.append(col)
        self.board = board

    def get_board_string(self):
        board = self.board
        board_string = ''
        board_string += self.generate_row_delimeter()
        for row in range(len(board)):
            for col in range(len(board[row])):
                board_string += board[row][col].value
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
        self.board[row][col].set_val(value)

    def get_cell_value(self, row, col):
        return self.board[row][col].value

    def fill_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col].set_val('*')

    def is_board_full(self):
        for row in self.board:
            for col in row:
                if not col.is_set():
                    return False
        return True

    def is_horizontal_win(self):
        for row in self.board:
            if self.list_has_match(row):
                return row[0]
        return False

    def list_has_match(self, input_list):
        result = input_list.count(input_list[0]) == len(input_list)
        if result:
            return input_list[0]
        return False
