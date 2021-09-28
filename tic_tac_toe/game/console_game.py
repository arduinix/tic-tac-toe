from .board import Board
from .game_actions import GameActions


class ConsoleGame(object):

    def __init__(self, game_id=""):
        self.play_game()
    
    def play_game(self):
        print('Welcome to Tic Tac Toe!')
        game = GameActions()

        board_size_input = input(game.get_message('board_size'))
        board_size = int(board_size_input) if board_size_input != '' else 3

        game.start_game(board_size=board_size)

        print(game.board.get_board_string())

        while not game.board.is_board_full() and not game.board.is_win():
            print("Player {}'s turn".format(game.get_current_player()))

            input_accepted = False
            while not input_accepted:
                player_turn = input(game.get_message('coordinate_entry'))
                row, col = player_turn.split(',')
                if not game.board.is_cell_set(int(row), int(col)):
                    input_accepted = True
                else:
                    print("The cell ({},{}) has already been played. Select another cell.".format(row, col))

            print('Player {} played row {}, col {}'.format(game.get_current_player(), row, col))
            
            game.play_cell(int(row), int(col))
            print(game.board.get_board_string())
            game.switch_player()

            if game.board.is_board_full():
                print(game.get_message('board_full'))

            if game.board.is_win():
                print('Player {} wins!'.format(game.board.is_win()))
