from tic_tac_toe.game import Game

expected_board_string = "-+-+-\n | | " \
                        "\n-+-+-\n | | "\
                        "\n-+-+-\n | | "\
                        "\n-+-+-\n"


class TestGame:
    def set_starting_player(self):
        "Get a random starting player from the game class"

        ttt_game = Game()

        ttt_game.get_starting_player()

        assert ttt_game.get_random_player() in ['X', 'O']

    def test_change_current_player(self):
        "If the current player is X player should switch to O and visa versa"

        ttt_game = Game()
        current_player = ttt_game.get_current_player()
        ttt_game.switch_player()
        next_player = ttt_game.get_current_player()

        assert current_player != next_player

    def test_start_stop_game(self):
        played_row = 2
        played_col = 2
        board_size = 3
        "A game should be started and an empty game board should be returned"
        "Player is able to play a board cell row {} col {}".format(str(played_row), str(played_col))

        ttt_game = Game()
        ttt_game.start_game(board_size=board_size)
        board_string = ttt_game.get_game_board().get_board_string()
        current_player = ttt_game.get_current_player()
        ttt_game.play_cell(played_row, played_col)

        assert board_string == expected_board_string
        assert ttt_game.is_game_running is True
        assert ttt_game.board.get_cell_mark(played_row, played_col) == current_player

        ttt_game.stop_game()
        assert ttt_game.is_game_running is False

    def test_acceptable_played_cell_is_accepted(self):
        game = Game()
        game.start_game(board_size=3)
        result = game.play_cell(1, 1)

        assert result == 'accepted'

    def test_already_played_cell_is_not_accepted(self):
        game = Game()
        game.start_game(board_size=3)
        game.play_cell(1, 1)

        result = game.play_cell(1, 1)

        assert result != 'accepted'

    def test_playing_cell_not_on_board_throws_error(self):
        game = Game()
        game.start_game(board_size=3)
        result = game.play_cell(4, 4)

        assert result != 'accepted'
