import random

BOARD_SIZE = 10

SPY, BOMB, FLAG = 10, 0, 99
NPIECES = dict(zip(range(1, 10),
                  (1, 1, 2, 3, 4, 4, 4, 5, 8)) +
               [(SPY,1), (BOMB,6), (FLAG,1)])

def winner(a, b):
    """ returns the winner of  a -> b """
    ab = (a,b)

    if ab == (SPY,1): return SPY  # The only case in which order matters
    if BOMB in ab and 8 in ab: return 8  # 8's kill bombs

    return min(ab)  # All else follows rank


def beats(attacker, victim):
    return winner(attacker, victim) == attacker


def board_value(board, player):
    return random.randint(1, 100)

