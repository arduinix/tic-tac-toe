from tic_tac_toe.game import WinDetector
import factory
from pytest_factoryboy import register

from .board import BoardFactory


register(BoardFactory)


class WinDetectorFactory(factory.Factory):
    class Meta:
        model = WinDetector

    board = BoardFactory
