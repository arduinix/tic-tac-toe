class Cell:
    def __init__(self):
        self.value = ' '

    def set_val(self, value):
        self.value = value

    def is_set(self):
        if self.value == ' ':
            return False
        return True
