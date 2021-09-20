from ttt import Game

def test_passing_test():
    "Make sure that true is true to verify testing functionality"
    assert True == True

def test_game_welcome_message(capsys):
    w_message = "Welcome to Tic Tac Toe!"
    "Welcome message when starting a new game should read \"{}\"".format(w_message)
    ttt_game = Game()
    ttt_game.print_welcome()
    captured = capsys.readouterr()
    assert captured.out == "{}\n".format(w_message)