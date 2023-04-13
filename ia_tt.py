import random
import numpy as np
import math
import os
from gamefunctions import create_board, print_board, check_win, check_draw, check_valid, play

def alphabeta_tt(board, depth, alpha, beta, maximizing_player, player, transposition_table):
    """
    The minimax algorithm with alpha-beta pruning and futility pruning to find the best move for the player.

    Arguments:
        board: the current state of the board
        depth: the depth of the search tree
        alpha: the best value for the maximizing player found so far
        beta: the best value for the minimizing player found so far
        maximizing_player: whether the current player is the maximizing player or not
        player: the player for which we are finding the best move
        transposition_table: a dictionary that stores previously seen board states and their scores

    Returns:
        a tuple (score, move) where score is the score for the current move and move is the optimal move for the player
    """

    # Base cases
    board_str = ''.join([''.join(row) for row in board])
    if board_str in transposition_table:
        return transposition_table[board_str]
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
                # print(board)
                score, _ = alphabeta_tt(board, depth-1, alpha, beta, not maximizing_player, 'X' if player == 'O' else 'O', transposition_table)
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
                    transposition_table[board_str] = (best_score, best_move)
                    return best_score, best_move
                # Futility pruning
                if maximizing_player and best_score >= beta:
                    transposition_table[board_str] = (best_score, best_move)
                    return best_score, best_move
                elif not maximizing_player and best_score <= alpha:
                    transposition_table[board_str] = (best_score, best_move)
                    return best_score, best_move

    transposition_table[board_str] = (best_score, best_move)
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
                score -= 1000
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
                score -= 1000
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
                score -= 1000
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