from ..resources.constants import CONST_BOARD_DEFAULT_CHAR


class Cell:
    def __init__(self):
        self.value = CONST_BOARD_DEFAULT_CHAR

    def set_val(self, value):
        self.value = value

    def is_set(self):
        if self.value == CONST_BOARD_DEFAULT_CHAR:
            return False
        return True

    def get_default_char(self):
        return CONST_BOARD_DEFAULT_CHAR
