import random
import numpy as np
import math
import os
from gamefunctions import create_board, print_board, check_win, check_draw, check_valid, play

'''
This game consists in a Tic Tac Toe game, where the player plays against the computer.

but it is not a simple Tic Tac Toe game, it is a 4x6 Tic Tac Toe game, where the player needs to make a line of 4 X's or O's to win.

The player can choose to play as X or O, and the computer will always play as the other one.

you still have the option to play against another player

now we gonna a ia using minimax algorithm

the algorithm receives a board and a player and a depth

the depth is the number of moves that the algorithm will see ahead

the algorithm will return the best move that the player can do for that board and that depth
'''

def alphabeta(board, depth, alpha, beta, maximizing_player, player):
    """
    The minimax algorithm with alpha-beta pruning and futility pruning to find the best move for the player.

    Arguments:
        board: the current state of the board
        depth: the depth of the search tree
        alpha: the best value for the maximizing player found so far
        beta: the best value for the minimizing player found so far
        maximizing_player: whether the current player is the maximizing player or not
        player: the player for which we are finding the best move

    Returns:
        a tuple (score, move) where score is the score for the current move and move is the optimal move for the player
    """

    # Base cases
    if check_draw(board):
        return 0, None
    elif depth == 0:
        return evaluate(board, player), None

    # Initialize the best score and move
    if maximizing_player:
        best_score = -math.inf
        best_move = None
    else:
        best_score = math.inf
        best_move = None

    # Loop over all valid moves
    for col in range(6):
        for row in range(4):
            if check_valid(board, col, row):
                # Make the move
                board[row][col] = player
                # Recursively call alphabeta on the next depth
                score, _ = alphabeta(board, depth-1, alpha, beta, not maximizing_player, 'X' if player == 'O' else 'O')
                # Undo the move
                # print(board)
                board[row][col] = ' '
                # Update the best score and move
                if maximizing_player:
                    if score > best_score:
                        best_score = score
                        best_move = (col, row)
                    alpha = max(alpha, best_score)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (col, row)
                    beta = min(beta, best_score)
                # Prune the search if alpha >= beta
                if alpha >= beta:
                    return best_score, best_move
                # Futility pruning
                if maximizing_player and best_score >= beta:
                    return best_score, best_move
                elif not maximizing_player and best_score <= alpha:
                    return best_score, best_move

    return best_score, best_move

def evaluate(board, player):
    """
    Evaluates the current state of the board for the given player.

    Arguments:
        board: the current state of the board
        player: the player for which we are evaluating the board

    Returns:
        a score representing the strength of the position for the player
    """

    # We'll use a simple scoring system based on the number of pieces in a row
    # of length 2, 3, and 4 for the player, as well as the number of pieces
    # in a row for the opponent

    score = 0

    # Check rows
    for row in range(4): # 0 1 2 3
        for col in range(3): # 0 1 2
            pieces = [board[row][col+i] for i in range(4)] # 0 1 2 3
            if pieces.count(player) == 4:
                score += 1000
            elif pieces.count(player) == 3 and pieces.count(' ') == 1:
                score += 10
            elif pieces.count(player) == 2 and pieces.count(' ') == 2:
                score += 1
            elif pieces.count(player) == 1 and pieces.count(' ') == 3:
                score += 0.1
            elif pieces.count(player) == 0 and pieces.count(' ') == 4:
                score += 0.01

            if pieces.count('X' if player == 'O' else 'O') == 4:
                score -= 10000
            elif pieces.count('X' if player == 'O' else 'O') == 3 and pieces.count(' ') == 1:
                score -= 10
            elif pieces.count('X' if player == 'O' else 'O') == 2 and pieces.count(' ') == 2:
                score -= 1
            elif pieces.count('X' if player == 'O' else 'O') == 1 and pieces.count(' ') == 3:
                score -= 0.1
            elif pieces.count('X' if player == 'O' else 'O') == 0 and pieces.count(' ') == 4:
                score -= 0.01

    # Check columns
    for col in range(6):
        for row in range(1):
            pieces = [board[row+i][col] for i in range(4)]
            if pieces.count(player) == 4:
                score += 1000
            elif pieces.count(player) == 3 and pieces.count(' ') == 1:
                score += 10
            elif pieces.count(player) == 2 and pieces.count(' ') == 2:
                score += 1
            elif pieces.count(player) == 1 and pieces.count(' ') == 3:
                score += 0.1
            elif pieces.count(player) == 0 and pieces.count(' ') == 4:
                score += 0.01

            if pieces.count('X' if player == 'O' else 'O') == 4:
                score -= 10000
            elif pieces.count('X' if player == 'O' else 'O') == 3 and pieces.count(' ') == 1:
                score -= 10
            elif pieces.count('X' if player == 'O' else 'O') == 2 and pieces.count(' ') == 2:
                score -= 1
            elif pieces.count('X' if player == 'O' else 'O') == 1 and pieces.count(' ') == 3:
                score -= 0.1
            elif pieces.count('X' if player == 'O' else 'O') == 0 and pieces.count(' ') == 4:
                score -= 0.01

    # Check diagonals
    for row in range(1):
        for col in range(3):
            pieces = [board[row+i][col+i] for i in range(4)]
            if pieces.count(player) == 4:
                score += 1000
            elif pieces.count(player) == 3 and pieces.count(' ') == 1:
                score += 10
            elif pieces.count(player) == 2 and pieces.count(' ') == 2:
                score += 1
            elif pieces.count(player) == 1 and pieces.count(' ') == 3:
                score += 0.1
            elif pieces.count(player) == 0 and pieces.count(' ') == 4:
                score += 0.01

            if pieces.count('X' if player == 'O' else 'O') == 4:
                score -= 10000
            elif pieces.count('X' if player == 'O' else 'O') == 3 and pieces.count(' ') == 1:
                score -= 10
            elif pieces.count('X' if player == 'O' else 'O') == 2 and pieces.count(' ') == 2:
                score -= 1
            elif pieces.count('X' if player == 'O' else 'O') == 1 and pieces.count(' ') == 3:
                score -= 0.1
            elif pieces.count('X' if player == 'O' else 'O') == 0 and pieces.count(' ') == 4:
                score -= 0.01

    for row in range(1):
        for col in range(3, 6):
            pieces = [board[row+i][col-i] for i in range(4)]
            if pieces.count(player) == 4:
                score += 10000
            elif pieces.count(player) == 3 and pieces.count(' ') == 1:
                score += 10
            elif pieces.count(player) == 2 and pieces.count(' ') == 2:
                score += 1
            elif pieces.count(player) == 1 and pieces.count(' ') == 3:
                score += 0.1
            elif pieces.count(player) == 0 and pieces.count(' ') == 4:
                score += 0.01

            if pieces.count('X' if player == 'O' else 'O') == 4:
                score -= 1000
            elif pieces.count('X' if player == 'O' else 'O') == 3 and pieces.count(' ') == 1:
                score -= 10
            elif pieces.count('X' if player == 'O' else 'O') == 2 and pieces.count(' ') == 2:
                score -= 1
            elif pieces.count('X' if player == 'O' else 'O') == 1 and pieces.count(' ') == 3:
                score -= 0.1
            elif pieces.count('X' if player == 'O' else 'O') == 0 and pieces.count(' ') == 4:
                score -= 0.01

    return score


