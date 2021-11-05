from .game_actions import GameActions
from .win_detection import WinDetector


class ConsoleGame(object):

    def __init__(self, game_id=""):
        self.play_game()

    def play_game(self):
        game = GameActions()
        print(game.get_message('welcome'))
        game_type_input = input(game.get_message('game_type'))
        game_type = int(game_type_input) if game_type_input != '' else 1
        board_size_input = input(game.get_message('board_size'))
        board_size = int(board_size_input) if board_size_input != '' else 3

        game.start_game(board_size=board_size, game_type=game_type)

        print(game.board.get_board_string())

        while not game.board.is_board_full() and not WinDetector(game.board).is_win():
            print("Player {}'s turn".format(game.get_current_player()))

            result = ""
            while result != 'accepted':
                player_turn = input(game.get_message('coordinate_entry'))
                row, col = player_turn.split(',')
                result = game.play_cell(int(row), int(col))
                if not result == 'accepted':
                    print(result)

            print('Player {} played row {}, col {}'.format(game.get_current_player(), row, col))
            print(game.board.get_board_string())

            if game.board.is_board_full():
                print(game.get_message('board_full'))
            win_detector = WinDetector(board=game.get_game_board())

            if win_detector.is_win():
                print('Player {} wins!'.format(win_detector.get_winner()))
