class WinDetector:
    def __init__(self, board):
        self.board = board

    @staticmethod
    def transpose_2d_list(input_list):
        transposed_list = []
        for index in range(len(input_list[0])):
            row = []
            for item in input_list:
                row.append(item[index])
            transposed_list.append(row)
        return transposed_list

    def is_horizontal_win(self):
        for row in self.board.board:
            if self.board.list_has_player_symbols(row):
                return row[0]
        return None

    def is_vertical_win(self):
        for row in self.transpose_2d_list(self.board):
            if self.list_has_player_symbols(row):
                return row[0]
        return False

    def is_top_diagonal_win(self):
        top_diagonal_list = []
        for index in range(self.board_size):
            top_diagonal_list.append(self.board[index][index])
        winner = self.list_has_player_symbols(top_diagonal_list)
        if winner:
            return winner
        return False

    def is_bottom_diagonal_win(self):
        bottom_diagonal_list = []
        row = self.board_size
        for col in range(self.board_size):
            bottom_diagonal_list.append(self.board[row - 1][col])
            row -= 1
        winner = self.list_has_player_symbols(bottom_diagonal_list)
        if winner:
            return winner
        return False

    def is_win(self):
        horizontal = self.is_horizontal_win()
        vertical = self.is_vertical_win()
        top_diagonal = self.is_top_diagonal_win()
        bottom_diagonal = self.is_bottom_diagonal_win()
        if horizontal:
            return horizontal
        elif vertical:
            return vertical
        elif top_diagonal:
            return top_diagonal
        elif bottom_diagonal:
            return bottom_diagonal
        else:
            return False
