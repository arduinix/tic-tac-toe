from .cell import Cell


class Board:
    def __init__(self, board_id=""):
        self.board_id = board_id
        self.board = {}
        self.initalize_board()

    def initalize_board(self):
        for c in range(1, 10, 1):
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
