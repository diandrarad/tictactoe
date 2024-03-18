"""
Tic Tac Toe Player
"""

import copy

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
    num_moves = sum(1 for row in board for cell in row if cell != EMPTY)
    return X if num_moves % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create a deep copy of the board
    new_board = copy.deepcopy(board)
    i, j = action

    # Check if the action is valid
    if board[i][j] != EMPTY:
        return ValueError("Invalid action")

    # Update the copied board with the player's move
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == X:
            return X
        elif board[0][col] == board[1][col] == board[2][col] == O:
            return O

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # Check if all cells have been filled
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check if the board is a terminal board
    if terminal(board):
        return None

    if player(board) == X:
        # Initialize best_value as negative infinity
        best_value = float('-inf')
        # Initialize best_action as None
        best_action = None

        # Iterate through each possible action on the board
        for action in actions(board):
            # Create a new board by applying the action
            new_board = result(board, action)
            # Recursively call the min_value function with the new board
            value = min_value(new_board)

            # Update best_value and best_action if a higher value is found
            if value > best_value:
                best_value = value
                best_action = action

    else:
        # Initialize best_value as positive infinity
        best_value = float('inf')
        best_action = None

        for action in actions(board):
            new_board = result(board, action)
            value = max_value(new_board)

            if value < best_value:
                best_value = value
                best_action = action

    return best_action


def min_value(board):
    """
    Returns the minimum utility value achievable for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    value = float('inf')

    for action in actions(board):
        new_board = result(board, action)
        value = min(value, max_value(new_board))

    return value


def max_value(board):
    """
    Returns the maximum utility value achievable for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    value = float('-inf')

    for action in actions(board):
        new_board = result(board, action)
        value = max(value, min_value(new_board))

    return value
