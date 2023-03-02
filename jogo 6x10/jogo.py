import random
import numpy as np
import math
import os
import time
from gamefunctions2 import create_board, print_board, check_win, check_draw, check_valid, play
from v4_ai import alphabeta_tt

board = create_board()

print('Welcome to Tic Tac Toe! 4x6 version')

print('You can play against the computer or against another player')
play_against = input('Do you want to play against the computer or against another player or do you want to watch the computer play against itself? (c/p/s): ')

if play_against == 'p':
    print('You are playing against another player')
    print('Player 1 will be X and Player 2 will be O')
    player1 = 'X'
    player2 = 'O'

    while True:
        print_board(board)
        print('Player 1')
        while True:
            col = int(input('Choose a column: '))
            line = int(input('Choose a line: '))
            if play(board, player1, col, line):
                break
            else:
                print('Invalid move, try again')
        if check_win(board, player1):
            print_board(board)
            print('Player 1 won!')
            break
        if check_draw(board):
            print_board(board)
            print('Draw!')
            break
        print_board(board)
        print('Player 2')
        while True:
            col = int(input('Choose a column: '))
            line = int(input('Choose a line: '))
            if play(board, player2, col, line):
                break
            else:
                print('Invalid move, try again')
        if check_win(board, player2):
            print_board(board)
            print('Player 2 won!')
            break
        if check_draw(board):
            print_board(board)
            print('Draw!')
            break

if play_against == 'c':
    print('You are playing against the computer')
    print('You will be X and the computer will be O')
    deep = int(input('Choose the depth of the search tree: '))
    player = 'X'
    computer = 'O'
    transposition_table = {}

    while True:
        print_board(board)
        print('Player')
        while True:
            col = int(input('Choose a column: '))
            line = int(input('Choose a line: '))
            if play(board, player, col, line):
                break
            else:
                print('Invalid move, try again')
        if check_win(board, player):
            print_board(board)
            print('Player won!')
            break
        if check_draw(board):
            print_board(board)
            print('Draw!')
            break
        print_board(board)
        print('Computer')
        while True:
            score, move = alphabeta_tt(board, deep, -math.inf, math.inf, True, computer, transposition_table)
            print('Score: ', score)
            col = move[0]
            line = move[1]
            if play(board, computer, col, line):
                break
            else:
                print('Invalid move, try again')
        if check_win(board, computer):
            print_board(board)
            print('Computer won!')
            break
        if check_draw(board):
            print_board(board)
            print('Draw!')
            break

if play_against == 's':
    print('You are watching the computer play against itself')
    print('The computer will be X and the computer will be O')
    deep = int(input('Choose the depth of the search tree: '))
    player = 'X'
    computer = 'O'
    transposition_table = {}

    while True:
        print_board(board)
        print('Computer 1')
        while True:
            score, move = alphabeta_tt(board, deep, -math.inf, math.inf, True, player, transposition_table)
            print('Score: ', score)
            col = move[0]
            line = move[1]
            if play(board, player, col, line):
                break
            else:
                print('Invalid move, try again')
        if check_win(board, player):
            print_board(board)
            print('Computer 1 won!')
            break
        if check_draw(board):
            print_board(board)
            print('Draw!')
            break
        print_board(board)
        print('Computer 2')
        while True:
            score, move = alphabeta_tt(board, deep, -math.inf, math.inf, True, computer, transposition_table)
            print('Score: ', score)
            col = move[0]
            line = move[1]
            if play(board, computer, col, line):
                break
            else:
                print('Invalid move, try again')
        if check_win(board, computer):
            print_board(board)
            print('Computer 2 won!')
            break
        if check_draw(board):
            print_board(board)
            print('Draw!')
            break