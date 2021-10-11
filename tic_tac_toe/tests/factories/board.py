from tic_tac_toe.game import Board
import factory
from pytest_factoryboy import register


class BoardFactory(factory.Factory):
    class Meta:
        model = Board
