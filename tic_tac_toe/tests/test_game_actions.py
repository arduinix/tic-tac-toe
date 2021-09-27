from tic_tac_toe.game import GameActions
from .constants import EXPECTED_GAME_BOARD_STRING


class TestGameActions:
    def test_get_welcome_message(self):
        excpected_welcome_message = "Welcome to Tic Tac Toe!"
        "Welcome message when starting a new game should read \"{}\"".format(excpected_welcome_message)

        actual_welcome_message = GameActions().get_welcome_message()

        assert excpected_welcome_message == actual_welcome_message

    def test_get_random_player(self):
        "Get a random starting player from the game class"

        ttt_game_actions = GameActions()

        assert ttt_game_actions.get_random_player() in ['X', 'O']

    def test_change_current_player(self):
        "If the current player is X player should switch to O and visa versa"

        ttt_game_actions = GameActions()
        current_player = ttt_game_actions.get_current_player()
        ttt_game_actions.switch_player()
        next_player = ttt_game_actions.get_current_player()

        assert current_player != next_player

    def test_get_game_board_string(self):
        "An empty, formatted Tic Tac Toe board should be returned"

        board_string = GameActions().get_game_board()

        assert board_string == EXPECTED_GAME_BOARD_STRING

    def test_play_board_cell(self):
        played_cell_number = 7
        "Player is able to play a board cell {}".format(str(played_cell_number))

        ttt_game_actions = GameActions()
        current_player = ttt_game_actions.get_current_player()
        ttt_game_actions.play_cell(played_cell_number)

        assert ttt_game_actions.board.get_cell_value(played_cell_number) == current_player
