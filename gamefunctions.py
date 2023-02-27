import random
from ia import *
import numpy as np
import math
import os

'''
This game consists in a Tic Tac Toe game, where the player plays against the computer.

but it is not a simple Tic Tac Toe game, it is a 4x6 Tic Tac Toe game, where the player needs to make a line of 4 X's or O's to win.

The player can choose to play as X or O, and the computer will always play as the other one.

you still have the option to play against another player
'''

def create_board():
    board = [[' ' for i in range(6)] for j in range(4)]
    return board

def print_board(board):
    #print the board
    for i in range(4):
        print('-------------------------')
        out = '| '
        for j in range(6):
            out += str(board[i][j]) + ' | '
        print(out)
    print('-------------------------')

def check_win(board, player):
    #check if the player won
    #check the rows
    for i in range(4):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    #check the columns
    for i in range(6):
        for j in range(1):
            if board[j][i] == player and board[j+1][i] == player and board[j+2][i] == player and board[j+3][i] == player:
                return True
    #check the diagonals
    for i in range(1):
        for j in range(3):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    for i in range(1):
        for j in range(3, 6):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True
    return False

def check_draw(board):
    #check if the game is a draw
    for i in range(4):
        for j in range(6):
            if board[i][j] == ' ':
                return False
    return True

def check_valid(board, col, line):
    #check if the player can play in the selected position
    if col < 0 or col > 5 or line < 0 or line > 3:
        return False
    if board[line][col] != ' ':
        return False
    return True

def play(board, player, col, line):
    #play the selected position
    if check_valid(board, col, line):
        board[line][col] = player
        return True
    return False



