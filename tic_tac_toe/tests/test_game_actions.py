from tic_tac_toe.game import GameActions
from .constants import EXPECTED_GAME_BOARD_STRING


class TestGameActions:
    def test_get_message(self):
        expected_message = "Welcome to Tic Tac Toe!"
        "Welcome message when starting a new game should read \"{}\"".format(expected_message)

        actual_message = GameActions().get_message('welcome')

        assert expected_message == actual_message

    def set_starting_player(self):
        "Get a random starting player from the game class"

        ttt_game = GameActions()

        ttt_game.get_starting_player()

        assert ttt_game.get_random_player() in ['X', 'O']

    def test_change_current_player(self):
        "If the current player is X player should switch to O and visa versa"

        ttt_game_actions = GameActions()
        current_player = ttt_game_actions.get_current_player()
        ttt_game_actions.switch_player()
        next_player = ttt_game_actions.get_current_player()

        assert current_player != next_player

    def test_start_stop_game(self):
        played_row = 2
        played_col = 2
        board_size = 3
        "A game should be started and an empty game board should be returned"
        "Player is able to play a board cell row {} col {}".format(str(played_row), str(played_col))

        ttt_game = GameActions()
        ttt_game.start_game(board_size=board_size)
        board_string = ttt_game.get_game_board()
        current_player = ttt_game.get_current_player()
        ttt_game.play_cell(played_row, played_col)

        assert board_string == EXPECTED_GAME_BOARD_STRING
        assert ttt_game.is_game_running is True
        assert ttt_game.board.get_cell_value(played_row, played_col) == current_player

        ttt_game.stop_game()
        assert ttt_game.is_game_running is False
