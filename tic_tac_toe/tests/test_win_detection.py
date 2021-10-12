from tic_tac_toe.game import WinDetector, Board
from .constants import TEST_SET_MARK
import pytest

set_value = TEST_SET_MARK


def test_transpose_2d_list():
    "Verify that a 2d list is transposed properly"

    input_list = [['A', 'B'], ['C', 'D']]
    expected_list = [['A', 'C'], ['B', 'D']]

    assert WinDetector.transpose_2d_list(input_list) == expected_list


def test_check_win_horizontal(BoardHorizontalWinFixture):
    "Fill the board with a horizontal pattern and check if it is identified as a win"

    win_detector = WinDetector(BoardHorizontalWinFixture)

    assert win_detector.is_horizontal_win() == set_value

    # def test_check_win_vertical(self):
    #     board_size = 3
    #     set_col = 1
    #     set_value = 'X'
    #     "Fill the board with a vertical pattern and check if it is identified as a win"

    #     board = Board(board_size=board_size)

    #     for row in range(board_size):
    #         board.set_cell(row, set_col, set_value)

    #     print(board.get_board_string())

    #     assert board.is_vertical_win() == set_value

    # def test_is_top_diagonal_win(self):
    #     board_size = 3
    #     set_value = 'X'
    #     "Fill the top diagonal of the board and check for a win"

    #     board = Board(board_size=board_size)

    #     for index in range(board_size):
    #         board.set_cell(index, index, set_value)

    #     print(board.get_board_string())

    #     assert board.is_top_diagonal_win() == set_value

    # def test_is_bottom_diagonal_win(self):
    #     board_size = 4
    #     set_value = 'X'
    #     "Fill the bottom diagonal of the board and check for a win"

    #     board = Board(board_size=board_size)

    #     row = board_size
    #     for col in range(board_size):
    #         board.set_cell(row - 1, col, set_value)
    #         row -= 1

    #     print(board.get_board_string())

    #     assert board.is_bottom_diagonal_win() == set_value

    # def test_check_is_win(self):
    #     board_size = 4
    #     set_value = 'X'
    #     "Fill the bottom diagonal of the board and check for a win"

    #     board = Board(board_size=board_size)

    #     row = board_size
    #     for col in range(board_size):
    #         board.set_cell(row - 1, col, set_value)
    #         row -= 1

    #     print(board.get_board_string())

    #     assert board.is_win() == set_value