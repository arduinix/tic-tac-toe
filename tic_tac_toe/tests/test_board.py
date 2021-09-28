from tic_tac_toe.game import Board
from .constants import EXPECTED_GAME_BOARD_STRING


class TestBoard:
    def test_get_formatted_board_string(self):
        "An empty, formatted Tic Tac Toe board should be returned"

        board_string = Board(board_size=3).get_board_string()
        print(board_string)

        assert board_string == EXPECTED_GAME_BOARD_STRING

    def test_set_cell(self):
        set_value = 'X'
        set_row = 2
        set_col = 2
        "Set a cell on the board and verify that the cell is set"

        board = Board()
        board.set_cell(set_row, set_col, set_value)

        assert board.get_cell_value(set_row, set_col) == set_value

    def test_get_board_size(self):
        specified_board_size = 9
        "Verify that the size of the board is properly returned"

        board = Board(board_size=specified_board_size)

        assert board.board_size == specified_board_size

    def test_check_board_is_full(self):
        "Fill the board and verify that the board shows as full"

        board = Board()
        board.fill_board()

        assert board.is_board_full()
