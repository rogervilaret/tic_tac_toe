"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in board:
        for a in row:
            if a==X:
                countX= countX + 1
            elif a==O:
                countO= countO + 1


    if countX > countO:
       return O
    else:  
       return X

    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    movements = set()
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                movements.add((i,j))    
    
    
    return movements
    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board[action[0]][action[1]] = player(board)
    return board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # check horitzontal winner
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]

    # check vertical winner
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    # check diagonal1 winner
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not EMPTY:
            return board[0][0]
    
    # check diagonal2 winner
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] is not EMPTY:
            return board[0][2]
    
    return EMPTY
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check winner
    if winner(board) is not None:
        return True

    # Check full board
    for row in board:
        for a in row:
            if a == EMPTY:
                return False

    return True
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)

    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0


    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    import copy
    
    def max_value(board1, pruning, who):
        
        if terminal(board1):
            return utility(board1)
        v = -2
        for act in actions(board1):
            board_op = copy.deepcopy(board1)
            vop = copy.copy(v)
            v = max(vop,min_value(result(board_op,act), pruning, who))
            #who is pruning?
            if who == O:
                if v > pruning:
                    return v
                    
        return v
    
    def min_value(board1, pruning, who):
        
        if terminal(board1):
            return utility(board1)
        v = +2
        for act in actions(board1):
            board_op = copy.deepcopy(board1)
            vop = copy.copy(v)
            v = min(vop,max_value(result(board_op,act),pruning, who))
            #who is pruning?
            if who == X:
                if v < pruning:
                    return v
                    
        return v
    
    
    posibilitats = set()
    #Starts analysing each posibility
    play = player(board)
    
    if play == X:
        pruning = -2
        for jugada in actions(board):
            board_test = copy.deepcopy(board)
            mov_util = (jugada,min_value(result(board_test,jugada),pruning,play))
            posibilitats.add(mov_util)
            if mov_util[1] > pruning:
                pruning = mov_util[1]
    else:
        pruning = 2
        for jugada in actions(board):
            board_test = copy.deepcopy(board)
            mov_util = (jugada,max_value(result(board_test,jugada),pruning,play))
            posibilitats.add(mov_util)
                     
            if mov_util[1] < pruning:
                pruning = mov_util[1]

    #search the best option
    next_move = None
    
    if play == X:
        ref = -2
        for valor in posibilitats:
            if valor[1] > ref:
                next_move= valor[0]
                ref = valor[1]
    else:
        ref = 2
        for valor in posibilitats:
            if valor[1] < ref:
                next_move= valor[0]
                ref = valor[1]

    return next_move
    raise NotImplementedError
