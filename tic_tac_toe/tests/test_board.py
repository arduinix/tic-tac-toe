from tic_tac_toe.game import Board
from .constants import EXPECTED_GAME_BOARD_STRING


class TestBoard:
    def test_get_formatted_board_string(self):
        "An empty, formatted Tic Tac Toe board should be returned"

        board_string = Board().get_board_string()

        assert board_string == EXPECTED_GAME_BOARD_STRING

    def test_set_cell(self):
        set_value = 'X'
        "Set a cell on the board and verify that the cell is set"

        board = Board()
        random_cell = board.get_random_cell_number()
        board.set_cell(random_cell, set_value)

        assert board.get_cell_value(random_cell) == set_value
    
    def test_get_board_size(self):
        specified_board_size = 9
        "Verify that the size of the board is properly returned"
        
        board = Board(board_size=specified_board_size)
        
        assert board.board_size == specified_board_size

    def test_check_board_is_full(self):
        "Fill the board and verify that the board shows as full"

        board = Board()
        for i in range(1, board.board_size + 1, 1):
            board.set_cell(i, 'X')

        assert board.is_board_full()

