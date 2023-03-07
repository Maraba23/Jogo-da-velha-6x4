import random
import numpy as np
import math
import os
import json
import time
from gamefunctions2 import create_board, print_board, check_win, check_draw, check_valid, play
from v4_ai import alphabeta_tt
import time


'''
The game will be played at jogo.py file and here we will only define the AI
The AI is a Q-Learning algorithm that will learn to play the game by itself
The q-table will be saved in a json file and loaded when the game is played
the json file will is called q_table.json
The AI will read the q-table and choose the best action based on learned values
If the q-table is does not present the current state, the AI will explore the environment
and learn the best action for the current state
the board will be passed as a function parameter argument
'''

############################################################################################################

BOARD_ROWS = 6
BOARD_COLS = 10

LEARNING_RATE = 0.5
DISCOUNT = 0.9
EXPLORE_RATE = 0.2

WIN_REWARD = 1
LOSE_REWARD = 0.01
DRAW_REWARD = 0.5

NUM_ACTIONS = BOARD_ROWS * BOARD_COLS


def load_q_table():
    #load the q-table from the json file
    if os.path.isfile('q_table.json'):
        with open('q_table.json') as f:
            q_table = json.load(f)
    else:
        q_table = {}
    return q_table

def save_q_table(q_table):
    #save the q-table in a json file
    with open('q_table.json', 'w') as f:
        json.dump(q_table, f)

def update_q_table(q_table, board, reward, next_board):
    #update the q-table
    #if the current state is not in the q-table, add it
    if str(board) not in q_table:
        q_table[str(board)] = reward
    #if the next state is not in the q-table, add it
    if str(next_board) not in q_table:
        q_table[str(next_board)] = reward
    #update the q-table
    q_table[str(board)] = q_table[str(board)] + LEARNING_RATE * (reward + DISCOUNT * np.max(q_table[str(next_board)]) - q_table[str(board)])

    return q_table

def get_action(q_table, board, explore_rate):
    #choose the best action based on the q-table
    #if the current state is not in the q-table, explore the environment
    if str(board) not in q_table.keys():
        return random.randint(0, NUM_ACTIONS-1), q_table
    #choose the best action based on the q-table
    if random.random() < explore_rate:
        return random.randint(0, NUM_ACTIONS-1), q_table
    else:
        return np.argmax(q_table[str(board)]), q_table

def get_next_board(board, action):
    #get the next board based on the action
    next_board = board
    if next_board[action//BOARD_COLS][action%BOARD_COLS] == ' ':
        next_board[action//BOARD_COLS][action%BOARD_COLS] = 'O'
    else:
        return None, None
    return next_board, (action//BOARD_COLS, action%BOARD_COLS)

def get_reward(board, next_board):
    #get the reward based on the next board
    reward = 0
    # check rows
    for row in range(len(board)):
        for col in range(len(board[row]) - 3):
            pieces = [board[row][col], board[row][col+1], board[row][col+2], board[row][col+3]]
            if pieces.count('O') == 4:
                reward += WIN_REWARD*2
            elif pieces.count('O') == 3 and pieces.count(' ') == 1:
                reward += WIN_REWARD
            elif pieces.count('O') == 2 and pieces.count(' ') == 2:
                reward += WIN_REWARD/2
            elif pieces.count('O') == 1 and pieces.count(' ') == 3:
                reward += WIN_REWARD/4
            
            if pieces.count('X') == 4:
                reward += LOSE_REWARD/4
            elif pieces.count('X') == 3 and pieces.count(' ') == 1:
                reward += LOSE_REWARD/2
            elif pieces.count('X') == 2 and pieces.count(' ') == 2:
                reward += LOSE_REWARD
            elif pieces.count('X') == 1 and pieces.count(' ') == 3:
                reward += LOSE_REWARD*2

    # check columns
    for row in range(len(board) - 3):
        for col in range(len(board[row])):
            pieces = [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]]
            if pieces.count('O') == 4:
                reward += WIN_REWARD*2
            elif pieces.count('O') == 3 and pieces.count(' ') == 1:
                reward += WIN_REWARD
            elif pieces.count('O') == 2 and pieces.count(' ') == 2:
                reward += WIN_REWARD/2
            elif pieces.count('O') == 1 and pieces.count(' ') == 3:
                reward += WIN_REWARD/4

            if pieces.count('X') == 4:
                reward += LOSE_REWARD/4
            elif pieces.count('X') == 3 and pieces.count(' ') == 1:
                reward += LOSE_REWARD/2
            elif pieces.count('X') == 2 and pieces.count(' ') == 2:
                reward += LOSE_REWARD
            elif pieces.count('X') == 1 and pieces.count(' ') == 3:
                reward += LOSE_REWARD*2

    # check diagonals
    for row in range(len(board) - 3):
        for col in range(len(board[row]) - 3):
            pieces = [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]]
            if pieces.count('O') == 4:
                reward += WIN_REWARD*2
            elif pieces.count('O') == 3 and pieces.count(' ') == 1:
                reward += WIN_REWARD
            elif pieces.count('O') == 2 and pieces.count(' ') == 2:
                reward += WIN_REWARD/2
            elif pieces.count('O') == 1 and pieces.count(' ') == 3:
                reward += WIN_REWARD/4

            if pieces.count('X') == 4:
                reward += LOSE_REWARD/4
            elif pieces.count('X') == 3 and pieces.count(' ') == 1:
                reward += LOSE_REWARD/2
            elif pieces.count('X') == 2 and pieces.count(' ') == 2:
                reward += LOSE_REWARD
            elif pieces.count('X') == 1 and pieces.count(' ') == 3:
                reward += LOSE_REWARD*2

    for row in range(len(board) - 3):
        for col in range(3, len(board[row])):
            pieces = [board[row][col], board[row+1][col-1], board[row+2][col-2], board[row+3][col-3]]
            if pieces.count('O') == 4:
                reward += WIN_REWARD*2
            elif pieces.count('O') == 3 and pieces.count(' ') == 1:
                reward += WIN_REWARD
            elif pieces.count('O') == 2 and pieces.count(' ') == 2:
                reward += WIN_REWARD/2
            elif pieces.count('O') == 1 and pieces.count(' ') == 3:
                reward += WIN_REWARD/4

            if pieces.count('X') == 4:
                reward += LOSE_REWARD/4
            elif pieces.count('X') == 3 and pieces.count(' ') == 1:
                reward += LOSE_REWARD/2
            elif pieces.count('X') == 2 and pieces.count(' ') == 2:
                reward += LOSE_REWARD
            elif pieces.count('X') == 1 and pieces.count(' ') == 3:
                reward += LOSE_REWARD*2


    return reward



############################################################################################################



board = create_board()
print('Welcome to Tic Tac Toe! Rainforce Learning version')
print('Here you will play against the computer that uses Reinforcement Learning')
train = input('Do you want to train the computer? (y/n): ')

if train == 'n':

    player1 = 'X'
    computer = 'O'

    q_table = load_q_table()

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
        print('Computer')
        action, q_table = get_action(q_table, board, EXPLORE_RATE)
        next_board, move = get_next_board(board, action)
        while next_board is None:
            action, q_table = get_action(q_table, board, EXPLORE_RATE)
            next_board, move = get_next_board(board, action)
        next_board_str = str(next_board)
        reward = get_reward(board, next_board)
        q_table = update_q_table(q_table, board, reward, next_board_str)
        board = next_board
        if check_win(board, computer):
            print_board(board)
            print('Computer won!')
            break
        if check_draw(board):
            print_board(board)
            print('Draw!')
            break

    save_q_table(q_table)

else:
    while True:
        board = create_board()
        deep = 2
        transposition_table = {}
        alphabeta_ia = 'X'
        computer = 'O'

        q_table = load_q_table()

        while True:
            print_board(board)
            print('Alphabeta IA')
            while True:
                score, move = alphabeta_tt(board, deep, -math.inf, math.inf, True, alphabeta_ia, transposition_table)
                print('Score: ', score)
                col = move[0]
                line = move[1]
                if play(board, alphabeta_ia, col, line):
                    break
                else:
                    print('Invalid move, try again')
            if check_win(board, alphabeta_ia):
                print_board(board)
                print('Alphabeta IA won!')
                reward = LOSE_REWARD
                q_table = update_q_table(q_table, board, reward, next_board_str)
                print('Reward: ', reward)
                break
            if check_draw(board):
                print_board(board)
                print('Draw!')
                break

            print_board(board)
            print('Computer')
            action, q_table = get_action(q_table, board, EXPLORE_RATE)
            next_board, move = get_next_board(board, action)
            while next_board is None:
                action, q_table = get_action(q_table, board, EXPLORE_RATE)
                next_board, move = get_next_board(board, action)
            next_board_str = str(next_board)
            reward = get_reward(board, next_board)
            q_table = update_q_table(q_table, board, reward, next_board_str)
            board = next_board
            print('Reward: ', reward)
            if check_win(board, computer):
                print_board(board)
                print('Computer won!')
                break
            if check_draw(board):
                print_board(board)
                print('Draw!')
                break
        save_q_table(q_table)
        time.sleep(1)

        