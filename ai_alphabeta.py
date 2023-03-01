import random
import numpy as np
import math
import os
from gamefunctions import create_board, print_board, check_win, check_draw, check_valid, play

def alphabeta_old(board, depth, alpha, beta, maximizing_player, player):
    """
    The minimax algorithm with alpha-beta pruning to find the best move for the player.

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
    if check_win(board, 'X' if player == 'O' else 'O'):
        return -1, None
    elif check_win(board, player):
        return 1, None
    elif check_draw(board):
        return 0, None
    elif depth == 0:
        return 0, None

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
                score, _ = alphabeta_old(board, depth-1, alpha, beta, not maximizing_player, 'X' if player == 'O' else 'O')
                # print(board)
                # Undo the move
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

    return best_score, best_move