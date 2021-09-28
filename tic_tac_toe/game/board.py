from .cell import Cell
import random


class Board:
    def __init__(self, board_size=3, board_id=""):
        self.board_size = board_size
        self.board_id = board_id
        self.board = []
        self.initalize_board()

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
