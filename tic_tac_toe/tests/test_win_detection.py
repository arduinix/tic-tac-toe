from tic_tac_toe.game import WinDetector, Board
from .constants import TEST_SET_MARK, TEST_BOARD_SIZE


set_value = TEST_SET_MARK
_B = ' '
_X = 'X'
_O = 'O'


def test_win_detector_detects_horizontal_win():
    test_board = [[_X, _X, _X],
                  [_B, _B, _B],
                  [_B, _B, _B]]

    board_with_horizontal_win = Board(board=test_board)

    assert WinDetector(board_with_horizontal_win).is_horizontal_win() == _X


def test_win_detector_detects_vertical_win():
    test_board = [[_X, _O, _O],
                  [_B, _O, _B],
                  [_X, _O, _B]]

    board_with_vertical_win = Board(board=test_board)

    assert WinDetector(board_with_vertical_win).is_vertical_win() == _O


def test_win_detector_detects_top_diagonal_win():
    test_board = [[_X, _O, _O],
                  [_B, _X, _B],
                  [_B, _O, _X]]

    board_with_top_diagonal_win = Board(board=test_board)

    assert WinDetector(board_with_top_diagonal_win).is_top_diagonal_win() == _X


def test_win_detector_detects_bottom_diagonal_win():
    test_board = [[_X, _X, _O],
                  [_B, _O, _B],
                  [_O, _O, _X]]

    board_with_bottom_diagonal_win = Board(board=test_board)

    assert WinDetector(board_with_bottom_diagonal_win).is_bottom_diagonal_win() == _O


def test_is_win_when_passing_test_board():
    test_board = [[_X, _X, _O],
                  [_B, _O, _B],
                  [_O, _O, _X]]

    board_with_win = Board(board=test_board)

    assert WinDetector(board_with_win).is_win() == _O
