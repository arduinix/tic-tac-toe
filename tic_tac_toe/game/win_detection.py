class WinDetector:
    def __init__(self, board):
        self.board = board
        self.player_symbols = self.board.player_symbols
        self.winner = None

    @staticmethod
    def _transpose_2d_list(input_list):
        transposed_list = []
        for index in range(len(input_list[0])):
            row = []
            for item in input_list:
                row.append(item[index])
            transposed_list.append(row)
        return transposed_list

    def _list_has_player_symbols(self, input_list):
        result = input_list.count(input_list[0])

        if input_list[0] in self.player_symbols and result == len(input_list):
            return input_list[0]
        return None

    def _get_horizontal_winner(self):
        for row in self.board.board:
            if self._list_has_player_symbols(row):
                return row[0]
        return None

    def _get_vertical_win(self):
        for row in self._transpose_2d_list(self.board.board):
            if self._list_has_player_symbols(row):
                return row[0]
        return None

    def _get_top_diagonal_win(self):
        top_diagonal_list = []
        for index in range(self.board.board_size):
            top_diagonal_list.append(self.board.board[index][index])
        winner = self._list_has_player_symbols(top_diagonal_list)
        if winner:
            return winner
        return None

    def _get_bottom_diagonal_win(self):
        bottom_diagonal_list = []
        row = self.board.board_size
        for col in range(self.board.board_size):
            bottom_diagonal_list.append(self.board.board[row - 1][col])
            row -= 1
        winner = self._list_has_player_symbols(bottom_diagonal_list)
        if winner:
            return winner
        return False

    def get_winner(self):
        horizontal_winner = self._get_horizontal_winner()
        vertical_winner = self._get_vertical_win()
        top_diagonal_winner = self._get_top_diagonal_win()
        bottom_diagonal_winner = self._get_bottom_diagonal_win()
        if horizontal_winner:
            return horizontal_winner
        elif vertical_winner:
            return vertical_winner
        elif top_diagonal_winner:
            return top_diagonal_winner
        elif bottom_diagonal_winner:
            return bottom_diagonal_winner
        else:
            return None

    def is_win(self):
        if self.get_winner() is not None:
            return True
        return False
