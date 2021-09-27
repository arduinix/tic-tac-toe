from tic_tac_toe.game import GameActions


def run():
    game_actions = GameActions()
    print(game_actions.get_welcome_message())
    print(game_actions.get_game_board())
