from tic_tac_toe.game import Board

expected_board_string = \
    "-+-+-\n | | " \
    "\n-+-+-\n | | "\
    "\n-+-+-\n | | "\
    "\n-+-+-\n"
 
_B = ' '
_X = 'X'
_O = 'O'


def test_get_board_returns_passed_in_board():
    test_board = [[_X, _X, _X],
                  [_B, _B, _B],
                  [_B, _B, _B]]

    board_with_board_set = Board(board=test_board)

    assert board_with_board_set.get_board() == test_board


def test_get_board_string_returns_expected_string_for_3x3_board():
    board_string = Board(size=3).get_board_string()

    assert board_string == expected_board_string


def test_set_a_cell_and_verify_cell_is_set_true():
    set_row = 2
    set_col = 2

    board = Board()
    board.set_cell(set_row, set_col, _X)

    assert board.is_cell_set(set_row, set_col) is True


def test_set_a_cell_and_get_its_mark():
    set_row = 2
    set_col = 2

    board = Board()
    board.set_cell(set_row, set_col, _X)

    assert board.get_cell_mark(set_row, set_col) == _X


def test_get_board_size_returns_set_board_size():
    specified_board_size = 4

    board_with_set_size = Board(size=specified_board_size)

    assert board_with_set_size.get_size() == specified_board_size


def test_is_board_full_true_when_board_full():
    test_board = [[_X, _X, _X],
                  [_O, _O, _X],
                  [_O, _X, _O]]

    full_board = Board(board=test_board)

    assert full_board.is_board_full()


def test_is_board_full_false_when_board_not_full():
    test_board = [[_X, _X, _X],
                  [_O, _B, _X],
                  [_O, _X, _O]]

    non_full_board = Board(board=test_board)

    assert non_full_board.is_board_full() is False


def test_is_cell_set_when_setting_a_cell():
    board = Board()
    board.set_cell(0, 0, _X)

    assert board.is_cell_set(0, 0) is True
