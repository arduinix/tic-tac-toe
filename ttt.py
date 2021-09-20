class Cell:
        def __init__(self):
            self.value = ' '

        def set_val(self, value):
            self.value = value

        def is_set(self):
            if self.value == ' ':
                return False
            return True

class Game:
    def __init__(self, game_id=""):
        self.game_id = game_id

    def print_welcome(self, welcome_message="Welcome to Tic Tac Toe!"):
        print(welcome_message)

class Board:
    def __init__(self, board_id=""):
        self.board_id = board_id
        self.board = {}
        self.initalize_board()
    
    def initalize_board(self):
        # initialize the board
        for c in range(1, 10, 1):
            self.board[str(c)] = Cell()

    def get_board_data(self):
        return self.board
    
    def print_board(self):
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
        
        print(board_string)