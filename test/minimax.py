from lib import minimax
from functools import partial
import asciitree

INF = float('inf')

# from http://en.wikipedia.org/wiki/File:Minimax.svg
TREE = \
((((10, INF,),
   (5,),),
  ((-10,),),),
    
 (((7, 5,),
   (-INF,),),
  ((-7, -5,),),),)


# from http://en.wikipedia.org/wiki/File:Negamax_AlphaBeta.gif
TREE2 = \
((((5, 6),
   (7, 4, 5),),
  ((3,),),),
 (((6,),
   (6, 9),),
  ((7,),),),
 (((5,),),
  ((9, 8),
   (6,),),),)


def _make_tree(tup):
    def mknode(children, depth):
        player = (-1) ** depth
        new_node = partial(minimax.Node, player)

        if not isinstance(children, tuple):
            return new_node(value=children)

        return new_node(children=[mknode(x, depth+1) for x in children])

    return mknode(tup, 1)


def test_negamax():
    root_node = _make_tree(TREE2)
    print asciitree.draw_tree(root_node)

    print "\nHit enter to run algo"
    raw_input()

    print ("NEGAMAX", minimax.negamax(root_node))
    print asciitree.draw_tree(root_node)
    assert 1 == 2


if __name__ == '__main__':
    test_negamax()

