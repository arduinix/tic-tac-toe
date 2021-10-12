from tic_tac_toe.game import Board
import factory
from pytest_factoryboy import register


class BoardFactory(factory.Factory):

    class Meta:
        model = Board

    @classmethod
    def _prepare():
        board = super(BoardFactory)._prepare()
        board_size = 3
        set_row = 1
        set_value = 'X'
        for col in range(board_size):
            board.set_cell(set_row, col, set_value)
        return board
