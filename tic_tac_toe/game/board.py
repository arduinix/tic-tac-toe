from .cell import Cell
import random


class Board:
    def __init__(self, board_size=9, board_id=""):
        self.board_size = 9
        self.board_id = board_id
        self.board = {}
        self.initalize_board()

    def initalize_board(self):
        for c in range(1, self.board_size + 1, 1):
            self.board[str(c)] = Cell()

    def get_board_string(self):
        board = self.board
        board_string = ''
        for c in range(len(board.keys())):
            c += 1
            board_string += board[str(c)].value
            if not c % 3 == 0:
                board_string += '|'
            elif not c == 9:
                board_string += '\n'
            if c == 3 or c == 6:
                board_string += '-+-+-\n'
        return board_string + '\n'

    def get_random_cell_number(self):
        return random.randint(0, self.board_size)

    def set_cell(self, cell_number, value):
        self.board[str(cell_number)].set_val(value)

    def get_cell_value(self, cell_number):
        return self.board[str(cell_number)].value

    def is_board_full(self):
        for k, v in self.board.items():
            if not v.is_set():
                return False
        return True
