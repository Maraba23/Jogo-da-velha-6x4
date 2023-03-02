import random
from ia import *
import numpy as np
import math
import os

def create_board():
    board = [[' ' for i in range(10)] for j in range(6)]
    return board

def print_board(board):
    #print the board
    for i in range(6):
        print('---------------------------------------------')
        out = '| '
        for j in range(10):
            out += str(board[i][j]) + ' | '
        print(out)
    print('---------------------------------------------')

def check_win(board, player):
    #check if the player won
    #check the rows
    for i in range(6):
        for j in range(7):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    #check the columns
    for i in range(10):
        for j in range(3):
            if board[j][i] == player and board[j+1][i] == player and board[j+2][i] == player and board[j+3][i] == player:
                return True
    #check the diagonals
    for i in range(3):
        for j in range(7):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    for i in range(3):
        for j in range(7, 10):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True
    return False

def check_draw(board):
    #check if the game is a draw
    for i in range(6):
        for j in range(10):
            if board[i][j] == ' ':
                return False
    return True

def check_valid(board, col, line):
    #check if the player can play in the selected position
    if col < 0 or col > 9 or line < 0 or line > 5:
        return False
    if board[line][col] != ' ':
        return False
    return True

def play(board, player, col, line):
    #play the selected position
    if check_valid(board, col, line):
        board[line][col] = player
        return True
    