from termcolor import colored, cprint
import copy
from itertools import permutations

board_4x4 = [0,0,0,0]
board_8x8 = [0,0,0,0,0,0,0,0]
board_16x16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def pprint(board):
    for index in board:
        for i in range(len(board)):
            if i == index:
                print(colored("Q", "cyan"), end = " ")
            else:
                print(colored(".", "white"), end = " ")
        print()
    print()

def put(board, depth, index):
    tmp_board = copy.deepcopy(board)
    tmp_board[depth] = index
    return tmp_board

def is_valid_up_to(board, depth):
    current_queen = board[depth]
    for i in range(depth):
        if current_queen == board[i]:
            return False
        if current_queen == board[i] + (depth - i) or \
           current_queen == board[i] - (depth - i):
            return False
    return True

def is_valid(board):
    for i in range(len(board)):
        if is_valid_up_to(board, i) == False:
            return False
    return True

def recursive_search(board, depth):
    if depth == len(board):
        pprint(board)
        # input()
        return
    for i in range(len(board)):
        new_board = put(board, depth, i)
        if is_valid_up_to(new_board, depth):
            # pprint(new_board)
            # input()
            recursive_search(new_board, depth+1)

def pro_search(board):
    i = 0
    while i < 8:
        if (is_valid(board)):
            pprint(board)
            i -= 1
        if board[i] < 7:
            board[i] += 1
            i+=1


def dumb_search(board, depth):
    if depth == len(board):
        if is_valid(board):
            pprint(board)
        return
    for i in range(len(board)):
        new_board = put(board, depth, i)
        dumb_search(new_board, depth+1)

def itertool_search(board):
    for p in permutations([i for i in range(len(board))]):
        if is_valid(p):
            pprint(p)

recursive_search(board_8x8, 0)
# dumb_search(board_8x8, 0)
# itertool_search(board_8x8)
