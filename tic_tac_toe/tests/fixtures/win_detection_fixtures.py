from tic_tac_toe.game import WinDetector
import pytest


@pytest.fixture
def WinDetectorFixture():
    return WinDetector
