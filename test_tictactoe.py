from ttt import Game, Board, Cell

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

def test_initial_game_board(capsys):
    "Empty Tic Tac Toe board should be printed on the console"
    ttt_board = Board()
    ttt_board.print_board()
    captured = capsys.readouterr()
    assert captured.out == " | | \n-+-+-\n | | \n-+-+-\n | | \n"

def test_cell_create():
    init_cell_value = ' '
    "Make sure that a new cell is created with a value of {}".format(init_cell_value)
    cell = Cell()
    assert cell.value == init_cell_value

def test_cell_set_value():
    set_val = 'X'
    "Make sure that a cell value can be set to {}".format(set_val)
    cell = Cell()
    cell.set_val(set_val)
    assert cell.value == set_val
    assert cell.is_set()