from project.lib import Board


class TestBoard:
    def test_get_formatted_board_string(self):
        "An empty, formatted Tic Tac Toe board should be returned"

        board_string = Board().get_board_string()

        assert board_string == " | | \n-+-+-\n | | \n-+-+-\n | | \n"
