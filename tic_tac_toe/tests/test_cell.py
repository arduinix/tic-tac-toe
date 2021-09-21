from tic_tac_toe.lib import Cell


class TestCell:
    def test_cell_create(self):
        init_cell_value = ' '
        "Make sure that a new cell is created with a value of {}".format(init_cell_value)

        cell = Cell()

        assert cell.value == init_cell_value

    def test_cell_set_value(self):
        set_val = 'X'
        "Make sure that a cell value can be set to {}".format(set_val)

        cell = Cell()
        cell.set_val(set_val)

        assert cell.value == set_val
        assert cell.is_set()
