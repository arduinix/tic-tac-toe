from tic_tac_toe.game import WinDetector
from .constants import TEST_SET_MARK, TEST_BOARD_SIZE


set_value = TEST_SET_MARK


def test_list_has_player_symbols(WinDetectorFixture, Board3x3Fixture):
    "Check if the list passed contains symbols of current players"

    assert WinDetectorFixture(Board3x3Fixture).list_has_player_symbols(['X', 'X', 'X']) == 'X'
    assert WinDetectorFixture(Board3x3Fixture).list_has_player_symbols(['X', 'X', 'O']) is None


def test_transpose_2d_list(WinDetectorFixture):
    "Verify that a 2d list is transposed properly"

    input_list = [['A', 'B'], ['C', 'D']]
    expected_list = [['A', 'C'], ['B', 'D']]

    assert WinDetectorFixture.transpose_2d_list(input_list) == expected_list


def test_check_win_horizontal(BoardHorizontalWinFixture, WinDetectorFixture):
    "Fill the board with a horizontal pattern and check if it is identified as a win"

    assert WinDetectorFixture(BoardHorizontalWinFixture).is_horizontal_win() == set_value


def test_check_win_vertical(BoardVerticalWinFixture, WinDetectorFixture):
    "Fill the board with a vertical pattern and check if it is identified as a win"

    assert WinDetectorFixture(BoardVerticalWinFixture).is_vertical_win() == set_value


def test_is_top_diagonal_win(BoardTopDiagonalWinFixture, WinDetectorFixture):
    "Fill the top diagonal of the board and check for a win"

    assert WinDetectorFixture(BoardTopDiagonalWinFixture).is_top_diagonal_win() == set_value


def test_is_bottom_diagonal_win(BoardBottomDiagonalWinFixture, WinDetectorFixture):
    "Fill the bottom diagonal of the board and check for a win"

    assert WinDetectorFixture(BoardBottomDiagonalWinFixture).is_bottom_diagonal_win() == set_value


def test_check_is_win(BoardBottomDiagonalWinFixture, WinDetectorFixture):
    "Fill the bottom diagonal of the board and check for a win"

    assert WinDetectorFixture(BoardBottomDiagonalWinFixture).is_win() == set_value
