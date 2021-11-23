import random
from ..resources.constants import PLAYER_2_MARK, PLAYER_1_MARK, GAME_MESSAGES
from .board import Board
from .messager import Messager


class Game:

    def __init__(self, game_id=""):
        self.game_id = game_id
        self.board = None
        self.messager = Messager()
        self.board_size = 0
        self.is_game_running = False
        self.current_player = None
        self.win_detector = None

    def start_game(self, board_size):
        self.board = Board(size=board_size)
        self.messager = Messager(board_size=board_size)
        self.is_game_running = True
        self.set_starting_player()

    def stop_game(self):
        self.board = None
        self.is_game_running = False

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
        return input_validation_response

    def get_game_board(self):
        return self.board

    def _check_input_valid(self, row, col):
        if self.board.is_cell_set(row, col):
            return self.messager.generate_cell_already_played_message(row, col)

        if not self.board.is_cell_on_board(row, col):
            return self.messager.generate_cell_not_on_board_message(row, col)

        return 'accepted'
