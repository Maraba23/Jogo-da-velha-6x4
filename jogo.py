import random
from ia import *
from ai_alphabeta import *
from ai_minimax import *
from ia_tt import alphabeta_tt
import numpy as np
import math
import os
from gamefunctions import create_board, print_board, check_win, check_draw, check_valid, play
import time


'''
This game consists in a Tic Tac Toe game, where the player plays against the computer.

but it is not a simple Tic Tac Toe game, it is a 4x6 Tic Tac Toe game, where the player needs to make a line of 4 X's or O's to win.

The player can choose to play as X or O, and the computer will always play as the other one.

you still have the option to play against another player
'''

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
    print('Choeose witch algorithm you want to use as X')
    print('1 - Minimax')
    print('2 - Alpha Beta')
    print('3 - Alpha Beta with evaluation function')
    print('4 - Alpha Beta with Transposition Table')

    computer1 = input('Choose the algorithm: ')
    deep1 = int(input('Choose the depth of the search tree: '))

    print('Choeose witch algorithm you want to use as O')
    print('1 - Minimax')
    print('2 - Alpha Beta')
    print('3 - Alpha Beta with evaluation function')
    print('4 - Alpha Beta with Transposition Table')

    computer2 = input('Choose the algorithm: ')
    deep2 = int(input('Choose the depth of the search tree: '))

    player1 = 'X'
    player2 = 'O'
    transposition_table1 = {}
    transposition_table2 = {}

    while True:
        print_board(board)
        print('Player 1')
        while True:
            if computer1 == '1':
                score, move = minimax(board, deep1, True, player1)
            if computer1 == '2':
                score, move = alphabeta_old(board, deep1, -math.inf, math.inf, True, player1)
            if computer1 == '3':
                score, move = alphabeta(board, deep1, -math.inf, math.inf, True, player1)
            if computer1 == '4':
                score, move = alphabeta_tt(board, deep1, -math.inf, math.inf, True, player1, transposition_table1)
            col = move[0]
            line = move[1]
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
            if computer2 == '1':
                score, move = minimax(board, deep2, True, player2)
            if computer2 == '2':
                score, move = alphabeta_old(board, deep2, -math.inf, math.inf, True, player2)
            if computer2 == '3':
                score, move = alphabeta(board, deep2, -math.inf, math.inf, True, player2)
            if computer1 == '4':
                score, move = alphabeta_tt(board, deep1, -math.inf, math.inf, True, player1, transposition_table1)
            col = move[0]
            line = move[1]
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
