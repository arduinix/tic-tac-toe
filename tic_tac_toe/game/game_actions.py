import random
from ..resources.constants import CONST_O, CONST_X
from .board import Board


class GameActions(object):

    def __init__(self, game_id=""):
        self.game_id = game_id
        self.current_player = self.get_random_player()
        self.board = Board()

    def get_welcome_message(self, welcome_message="Welcome to Tic Tac Toe!"):
        return welcome_message

    def get_random_player(self):
        return random.choice([CONST_X, CONST_O])

    def get_current_player(self):
        return self.current_player

    def switch_player(self):
        if self.current_player == CONST_X:
            self.current_player = CONST_O
        else:
            self.current_player = CONST_X

    def get_game_board(self):
        return self.board.get_board_string()

    def play_cell(self, cell_number):
        self.board.set_cell(cell_number, self.current_player)
