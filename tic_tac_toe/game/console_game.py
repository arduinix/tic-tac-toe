import re
from .game import Game
from .win_detection import WinDetector


class ConsoleGame(object):

    def __init__(self, game_id=""):
        self.play_game()

    def play_game(self):
        game = Game()
        print(game.messager.get_message('welcome'))

        board_size_input = input(game.messager.get_message('board_size'))
        board_size = int(board_size_input) if board_size_input != '' else 3

        game.start_game(board_size=board_size)

        print(game.board.get_board_string())

        while not game.board.is_board_full() and not WinDetector(game.board).is_win():
            print("Player {}'s turn".format(game.get_current_player()))

            result = ""
            while not result == 'accepted':
                player_turn = input(game.messager.get_message('coordinate_entry'))
                if re.fullmatch('[0-9]+(,[0-9]+)', player_turn):
                    row, col = player_turn.split(',')
                    result = game.play_cell(int(row), int(col))
                else:
                    result = 'The entered string: \"{}\" is invalid. Use the form row,col.'.format(player_turn)
                if not result == 'accepted':
                    print(result)

            print('Player {} played row {}, col {}'.format(game.get_current_player(), row, col))
            print(game.board.get_board_string())
            game.switch_player()

            if game.board.is_board_full():
                print(game.messager.get_message('board_full'))
            win_detector = WinDetector(board=game.get_game_board())

            if win_detector.is_win():
                print('Player {} wins!'.format(win_detector.get_winner()))
