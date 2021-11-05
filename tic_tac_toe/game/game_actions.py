import random
from ..resources.constants import PLAYER_2_MARK, PLAYER_1_MARK, GAME_MESSAGES
from .board import Board


class GameActions:

    def __init__(self, game_id="", custom_messages={}):
        self.game_id = game_id
        self.messages = custom_messages | GAME_MESSAGES
        self.board = None
        self.board_size = 0
        self.is_game_running = False
        self.current_player = None
        self.win_detector = None

    def start_game(self, board_size, game_type=1):
        self.board = Board(size=board_size)
        self.game_type = game_type
        self.is_game_running = True
        self.set_starting_player()

    def stop_game(self):
        self.board = None
        self.is_game_running = False

    def get_message(self, message_name):
        return self.messages[message_name]

    def set_starting_player(self):
        self.current_player = self.get_random_player()

    def get_random_player(self):
        return random.choice([PLAYER_1_MARK, PLAYER_2_MARK])

    def get_current_player(self):
        return self.current_player

    def switch_player(self):
        if self.current_player == PLAYER_1_MARK:
            self.current_player = PLAYER_2_MARK
        else:
            self.current_player = PLAYER_1_MARK

    def play_cell(self, row, col):
        input_validation_response = self._check_input_valid(row, col)
        if input_validation_response == 'accepted':
            self.board.set_cell(row, col, self.current_player)
            self.switch_player()
        return input_validation_response

    def get_game_board(self):
        return self.board

    def _check_input_valid(self, row, col):
        cell_not_on_board = self._generate_cell_not_on_board_message(row, col)
        if cell_not_on_board:
            return cell_not_on_board

        cell_already_played = self._generate_cell_already_played_message(row, col)
        if cell_already_played:
            return cell_already_played

        return 'accepted'

    def _generate_cell_already_played_message(self, row, col):
        if self.board.is_cell_set(row, col):
            return "The cell ({},{}) has already been played. Select another cell.".format(row, col)
        return None

    def _generate_cell_not_on_board_message(self, row, col):
        if not self.board.is_cell_on_board(row, col):
            return "The cell ({r},{c}) is not on the board select another cell with a row,col from 0 to "\
                   "{s} in the format (0,0) to ({s},{s}).".format(r=row, c=col, s=self.board.size - 1)
        return None
