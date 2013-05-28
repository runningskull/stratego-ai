INF = float('inf')

class Node(object):
    def __init__(self, player, board=None, value=None, children=[]):
        self.player = player
        self.value = value
        self.board = board
        self.children = children

    def __str__(self):
        return ' ' + str(self.value or '?')

    def terminal(self):
        return not len(self.children)


def nval(node):
    return node.value or 0


def negamax(start_node, max_depth=99, heuristic=nval):
    def negamax_ab(node, depth, alpha, beta, color):
        if depth <= 0 or node.terminal():
            #return node.value or heuristic(node, start_node.player)
            return color * (node.value or heuristic(node, start_ode.player))

        for child in node.children:
            val = -negamax_ab(child, depth-1, -beta, -alpha, -color)
            node.value = abs(val)    # helpful for the printout

            if val >= beta: 
                return val

            if val > alpha: alpha = val

        return alpha

    return negamax_ab(start_node, max_depth, -INF, INF, 1)


def dumb_negamax(node, depth, alpha=-INF, beta=INF):
    if node.terminal() or (depth <= 0):
        return nval(node)

    record = -INF

    for child in node.children:
        score = -dumb_negamax(child, depth - 1)
        child.value = abs(score) # for printing

        if score > record:
            record = score

    node.value = record
    return record

