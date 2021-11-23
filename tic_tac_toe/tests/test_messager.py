from tic_tac_toe.game import Messager


def test_get_message():
    expected_message = "Welcome to Tic Tac Toe!"

    actual_message = Messager(board_size=3).get_message('welcome')

    assert expected_message == actual_message


def test_generate_cell_not_on_board_message_returns_expected_string():
    expected_message = "The cell (4,0) is not on the board. Select another cell with a row,col from 0 to "\
        "2 in the format (0,0) to (2,2)."

    messager = Messager(board_size=3)

    assert expected_message == messager.generate_cell_not_on_board_message(4, 0)


def test_generate_cell_already_played_message_returns_expected_string():
    expected_message = "The cell (1,1) has already been played. Select another cell."
    messager = Messager(board_size=3)

    assert expected_message == messager.generate_cell_already_played_message(1, 1)
