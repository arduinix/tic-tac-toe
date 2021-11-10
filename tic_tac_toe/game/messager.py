from ..resources.constants import GAME_MESSAGES


class Messager:
    def __init__(self, board_size, custom_messages={}):
        self.board_size = board_size
        self.messages = custom_messages | GAME_MESSAGES

    def get_message(self, message_name):
        return self.messages[message_name]

    def generate_cell_already_played_message(self, row, col):
        return "The cell ({},{}) has already been played. Select another cell.".format(row, col)

    def generate_cell_not_on_board_message(self, row, col):
        return "The cell ({r},{c}) is not on the board. Select another cell with a row,col from 0 to "\
            "{s} in the format (0,0) to ({s},{s}).".format(r=row, c=col, s=self.board_size - 1)
