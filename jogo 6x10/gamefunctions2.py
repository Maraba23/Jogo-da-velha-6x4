import random
import numpy as np
import math
import os

def create_board():
    board = [[' ' for i in range(10)] for j in range(6)]
    return board

def print_board(board):
    #print the board
    for i in range(6):
        print('-----------------------------------------')
        out = '| '
        for j in range(10):
            out += str(board[i][j]) + ' | '
        print(out)
    print('-----------------------------------------')

def check_win(board, player):
    #check if the player won
    #check the rows
    for row in range(len(board)):
        for col in range(len(board[row])-3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    #check the columns
    for row in range(len(board)-3):
        for col in range(len(board[row])):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    #check the diagonals
    for row in range(len(board)-3):
        for col in range(len(board[row])-3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    for row in range(len(board)-3):
        for col in range(len(board[row])-3):
            if board[row][col+3] == player and board[row+1][col+2] == player and board[row+2][col+1] == player and board[row+3][col] == player:
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
    