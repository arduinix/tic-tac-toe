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

    def start_game(self, board_size):
        self.board = Board(size=board_size)
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

    def get_game_board(self):
        return self.board.get_board_string()

    def play_cell(self, row, col):
        self.board.set_cell(row, col, self.current_player)
