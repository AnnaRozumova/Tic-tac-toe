import pytest
from game_mechanism import TicTacToe

def test_create_grid():
    game = TicTacToe()
    assert len(game.grid) == 9
    for cell in game.grid.values():
        assert cell == '_'


def test_move():
    game = TicTacToe()
    assert game.move('A1', 'X')
    assert not game.move('A1', 'O')
    assert game.grid['A1'] == 'X'

def test_check_win():
    game = TicTacToe()
    game.grid['A1'] = 'X'
    game.grid['B1'] = 'X'
    game.grid['C1'] = 'X'
    assert game.check_win()

    game.grid['C1'] = '_'
    assert not game.check_win()