from tic_tac_toe.lib import Game


def main():
    game = Game()
    print(game.get_welcome_message())
    print(game.get_game_board())


if __name__ == '__main__':
    main()
