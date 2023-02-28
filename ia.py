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

def minimax(board, player, depth):
    #check if the player won
    if check_win(board, player):
        return 1
    #check if the player lost
    if check_win(board, 'X' if player == 'O' else 'O'):
        return -1
    #check if the game is a draw
    if check_draw(board):
        return 0
    #check if the depth is 0
    if depth == 0:
        return 0
    #check if the player is X
    # computer is always O
    if player == 'X':
        best_value = -math.inf
        print('passando aqui #1')
        for i in range(4):
            for j in range(6):
                if board[i][j] == ' ':
                    board[i][j] = player
                    value = minimax(board, 'O', depth-1)
                    board[i][j] = ' '
                    best_value = max(best_value, value)
        return best_value
    #check if the player is O
    if player == 'O':
        best_value = math.inf
        print('passando aqui #2')
        for i in range(4):
            for j in range(6):
                if board[i][j] == ' ':
                    board[i][j] = player
                    print('passando aqui #5')
                    value = minimax(board, 'X', depth-1)
                    board[i][j] = ' '
                    best_value = min(best_value, value)
        return best_value


    
def ia(board, player, depth):
    #check if the player is X
    if player == 'X':
        best_value = -math.inf
        best_move = None
        print('passando aqui #3')
        for i in range(4):
            for j in range(6):
                if board[i][j] == ' ':
                    board[i][j] = player
                    value = minimax(board, 'O', depth-1)
                    board[i][j] = ' '
                    print(f'value: {value}, best_value: {best_value}, best_move: {best_move}')
                    if value > best_value:
                        best_value = value
                        best_move = (i, j)

        return best_move
    #check if the player is O
    if player == 'O':
        best_value = math.inf
        best_move = None
        print('passando aqui #4')
        for i in range(4):
            for j in range(6):
                if board[i][j] == ' ':
                    board[i][j] = player
                    print('passando aqui #5')
                    value = minimax(board, 'X', depth-1)
                    board[i][j] = ' '
                    print(f'value: {value}, best_value: {best_value}, best_move: {best_move}')
                    if value < best_value:
                        best_value = value
                        best_move = (i, j)

        return best_move




