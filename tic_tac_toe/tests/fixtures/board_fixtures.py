from tic_tac_toe.game import Board
from ..constants import TEST_SET_MARK, TEST_BOARD_SIZE, TEST_SET_ROW, TEST_SET_COL
import pytest

board_size = TEST_BOARD_SIZE
set_value = TEST_SET_MARK
set_row = TEST_SET_ROW
set_col = TEST_SET_COL


@pytest.fixture
def Board3x3Fixture():
    board = Board(board_size=board_size)
    return board


@pytest.fixture
def BoardHorizontalWinFixture(Board3x3Fixture):
    board = Board3x3Fixture
    for col in range(board_size):
        board.set_cell(set_row, col, set_value)
    return board


@pytest.fixture
def BoardVerticalWinFixture(Board3x3Fixture):
    board = Board3x3Fixture
    for row in range(board_size):
        board.set_cell(row, set_col, set_value)
    return board


@pytest.fixture
def BoardTopDiagonalWinFixture(Board3x3Fixture):
    board = Board3x3Fixture
    for index in range(board_size):
        board.set_cell(index, index, set_value)
    return board


@pytest.fixture
def BoardBottomDiagonalWinFixture(Board3x3Fixture):
    board = Board3x3Fixture
    row = board_size
    for col in range(board_size):
        board.set_cell(row - 1, col, set_value)
        row -= 1
    return board
