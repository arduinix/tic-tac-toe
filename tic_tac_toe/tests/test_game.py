from tic_tac_toe.lib import Game


class TestGame:
    def test_get_welcome_message(self):
        excpected_welcome_message = "Welcome to Tic Tac Toe!"
        "Welcome message when starting a new game should read \"{}\"".format(excpected_welcome_message)

        actual_welcome_message = Game().get_welcome_message()

        assert excpected_welcome_message == actual_welcome_message

    def test_get_random_player(self):
        "Get a random starting player from the game class"

        ttt_game = Game()

        assert ttt_game.get_random_player() in ['X', 'O']
    
    def test_change_current_player(self):
        "If the current player is X player should switch to O and visa versa"

        ttt_game = Game()
        current_player = ttt_game.get_current_player()
        ttt_game.swtich_player()
        next_player = ttt_game.get_current_player()

        assert current_player != next_player

        
