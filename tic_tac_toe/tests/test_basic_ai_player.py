from tic_tac_toe.game import BasicAiPlayer, Board


def test_basic_ai_player_returns_unset_mark():
    board = Board()
    ai_player = BasicAiPlayer(board=board)

    unset_mark = ai_player.get_unset_mark()

    assert board.is_cell_set(unset_mark.row, unset_mark.col) is False
