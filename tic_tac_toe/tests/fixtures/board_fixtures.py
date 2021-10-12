from tic_tac_toe.game import Board
import pytest

board_size = 3

@pytest.fixture
def Board3x3Fixture():
    board = Board(board_size=board_size)
    return board

@pytest.fixture
def BoardHorizontalWinFixture(Board3x3Fixture):
    board = Board3x3Fixture
    set_row = 1
    set_value = 'X'
    for col in range(board_size):
        board.set_cell(set_row, col, set_value)
    return board
