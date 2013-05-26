import unittest
from lib.stratego import *

def test_winner():
    assert winner(1, 3) == 1
    assert winner(3, 1) == 1

    assert winner(SPY, 1) == SPY
    assert winner(1, SPY) == 1

    assert winner(3, BOMB) == BOMB
    assert winner(8, BOMB) == 8

    assert winner(1, FLAG) == 1
    assert winner(9, FLAG) == 9
    assert winner(SPY, FLAG) == SPY


def test_beats():
    assert beats(1, 3)
    assert not beats(3, 1)
