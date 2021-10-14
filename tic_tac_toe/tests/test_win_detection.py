from tic_tac_toe.game import WinDetector, Board

_B = ' '
_X = 'X'
_O = 'O'


def test_win_detector_detects_horizontal_win():
    test_board = [[_X, _X, _X],
                  [_B, _B, _B],
                  [_B, _B, _B]]

    board_with_horizontal_win = Board(board=test_board)

    assert WinDetector(board_with_horizontal_win).is_win() is True
    assert WinDetector(board_with_horizontal_win).get_winner() == _X


def test_win_detector_detects_vertical_win():
    test_board = [[_X, _O, _O],
                  [_B, _O, _B],
                  [_X, _O, _B]]

    board_with_vertical_win = Board(board=test_board)

    assert WinDetector(board_with_vertical_win).is_win() is True
    assert WinDetector(board_with_vertical_win).get_winner() == _O


def test_win_detector_detects_top_diagonal_win():
    test_board = [[_X, _O, _O],
                  [_B, _X, _B],
                  [_B, _O, _X]]

    board_with_top_diagonal_win = Board(board=test_board)

    assert WinDetector(board_with_top_diagonal_win).is_win() is True
    assert WinDetector(board_with_top_diagonal_win).get_winner() == _X


def test_win_detector_detects_bottom_diagonal_win():
    test_board = [[_X, _X, _O],
                  [_B, _O, _B],
                  [_O, _O, _X]]

    board_with_bottom_diagonal_win = Board(board=test_board)

    assert WinDetector(board_with_bottom_diagonal_win).is_win() is True
    assert WinDetector(board_with_bottom_diagonal_win).get_winner() == _O
