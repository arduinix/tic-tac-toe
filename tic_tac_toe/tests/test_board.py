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
        set_value = 'X'
        "Fill the board and verify that the board shows as full"

        board = Board()
        for row in range(board.board_size):
            for col in range(board.board_size):
                board.set_cell(row, col, set_value)

        assert board.is_board_full()

    def test_check_win_horizontal(self):
        board_size = 3
        set_row = 1
        set_value = 'X'
        "Fill the board with a horizontal pattern and check if it is identified as a win"

        board = Board(board_size=board_size)

        for col in range(board_size):
            board.set_cell(set_row, col, set_value)

        print(board.get_board_string())

        assert board.is_horizontal_win() == set_value

    def test_list_has_wins(self):
        "Check if the list_has_match method returns the desired result"

        board = Board()

        assert board.list_has_wins(['X', 'X', 'X']) == 'X'
        assert board.list_has_wins(['X', 'X', 'O']) is False

    def test_transpose_2d_list(self):
        "Verify that a 2 list is transposed properly"
        board = Board()

        input_list = [['A', 'B'], ['C', 'D']]
        expected_list = [['A', 'C'], ['B', 'D']]

        print(board.transpose_2d_list(input_list))

        assert board.transpose_2d_list(input_list) == expected_list

    def test_check_win_vertical(self):
        board_size = 3
        set_col = 1
        set_value = 'X'
        "Fill the board with a vertical pattern and check if it is identified as a win"

        board = Board(board_size=board_size)

        for row in range(board_size):
            board.set_cell(row, set_col, set_value)

        print(board.get_board_string())

        assert board.is_vertical_win() == set_value

    def test_is_top_diagonal_win(self):
        board_size = 3
        set_value = 'X'
        "Fill the top diagonal of the board and check for a win"

        board = Board(board_size=board_size)

        for index in range(board_size):
            board.set_cell(index, index, set_value)

        print(board.get_board_string())

        assert board.is_top_diagonal_win() == set_value

    def test_is_bottom_diagonal_win(self):
        board_size = 4
        set_value = 'X'
        "Fill the bottom diagonal of the board and check for a win"

        board = Board(board_size=board_size)

        row = board_size
        for col in range(board_size):
            board.set_cell(row - 1, col, set_value)
            row -= 1

        print(board.get_board_string())

        assert board.is_bottom_diagonal_win() == set_value

    def test_check_is_win(self):
        board_size = 4
        set_value = 'X'
        "Fill the bottom diagonal of the board and check for a win"

        board = Board(board_size=board_size)

        row = board_size
        for col in range(board_size):
            board.set_cell(row - 1, col, set_value)
            row -= 1

        print(board.get_board_string())

        assert board.is_win() == set_value

    def test_is_cell_set(self):
        "Set a cell and verify that it is set"

        board = Board()
        board.set_cell(0, 0, 'X')

        assert board.is_cell_set(0, 0) is True
