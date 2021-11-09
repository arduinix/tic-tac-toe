from .mark import Mark
import random


class BasicAiPlayer:
    def __init__(self, board):
        self.board = board

    def get_unset_mark(self):
        found_unset = False
        while not found_unset:
            row = self.get_rand()
            col = self.get_rand()

            if not self.board.is_cell_set(row, col):
                found_unset = True

        return(Mark(row, col))

    def get_rand(self):
        return random.randint(0, self.board.size - 1)
