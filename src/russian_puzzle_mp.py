from termcolor import colored, cprint
import numpy as np
import time

cmap = {
'A':'red',
'B':'green',
'C':'yellow',
'D':'blue',
'E':'magenta',
'F':'cyan',
'G':'white',
'H':'red',
'L':'green',
'M':'yellow',
'N':'blue',
'O':'magenta',
'X':'cyan',
'.':'white',
}

def pprint(piece):
    if(piece == False):
        print(False)
        return

    for row in piece:
        for char in row:
            print(colored(char, cmap[char]), end = " ")
        print()
    print()

def pieces_print(pieces):
    for piece in pieces:
        pprint(piece)

def rotate(piece):
    return tuple(zip(*piece[::-1]))

def add_rotations(piece):
    for i in range(3):
        piece.append(rotate(piece[i]))

def add_rotations_of(piece, of):
    tmp = []
    tmp.append(of)
    for i in range(3):
        tmp.append(rotate(tmp[i]))
    for j in range(4):
        piece.append(tmp[j])

def add_rotations_and_mirrors(piece):
    add_rotations(piece)
    add_rotations_of(piece, mirror(piece[0]))


def mirror(piece):
    return piece[::-1]

a_piece = []
a_piece.append((
('.','A','.',),
('A','A','A',),
('.','A','.',),
))
a_piece_thicc = []
a_piece_thicc.append((
('.','A','.','.','.','.','.',),
('A','A','A','.','.','.','.',),
('.','A','.','.','.','.','.',),
('.','.','.','.','.','.','.',),
('.','.','.','.','.','.','.',),
))

b_piece = []
b_piece.append((
('B','B',),
('B','.',),
('B','B',),
))
add_rotations(b_piece)


c_piece = []
c_piece.append((
('C','.','.',),
('C','C','.',),
('.','C','C',),
))
add_rotations(c_piece)

d_piece = []
d_piece.append((
('D','D','D','D','D',),
))
d_piece.append(rotate(d_piece[0]))

e_piece = []
e_piece.append((
('E','E','E',),
('.','E','.',),
('.','E','.',),
))
add_rotations(e_piece)

f_piece = []
f_piece.append((
('F','F','F',),
('F','F','.',),
))
add_rotations_and_mirrors(f_piece)

g_piece = []
g_piece.append((
('.','G','.',),
('.','G','G',),
('G','G','.',),
))
add_rotations_and_mirrors(g_piece)

h_piece = []
h_piece.append((
('.','.','H','H',),
('H','H','H','.',),
))
add_rotations_and_mirrors(h_piece)

l_piece = []
l_piece.append((
('.','.','.','L',),
('L','L','L','L',),
))
add_rotations_and_mirrors(l_piece)

m_piece = []
m_piece.append((
('.','.','M','.',),
('M','M','M','M',),
))
add_rotations_and_mirrors(m_piece)

n_piece = []
n_piece.append((
('.','N','N',),
('.','N','.',),
('N','N','.',),
))
n_piece.append(rotate(n_piece[0]))
n_piece.append(mirror(n_piece[0]))
n_piece.append(mirror(rotate(n_piece[0])))

o_piece = []
o_piece.append((
('O','O','O',),
('O','.','.',),
('O','.','.',),
))
o_piece.append(rotate(o_piece[0]))
o_piece.append(mirror(o_piece[0]))
o_piece.append(mirror(rotate(o_piece[0])))

pieces = [
# tuple(a_piece_thicc),
tuple(b_piece),
tuple(c_piece),
tuple(g_piece),
tuple(e_piece),
tuple(f_piece),
tuple(n_piece),
tuple(o_piece),
tuple(h_piece),
tuple(l_piece),
tuple(m_piece),
tuple(d_piece),
]

# for p in pieces:
#     pieces_print(p)
#1pprint(mirror(b_piece[1]))
import copy

def put(board, piece, r, c):
    tmp_board = copy.deepcopy(board)
    try:
        for i, row in enumerate(piece):
            for j, char in enumerate(row):
                if(char == '.'):
                    pass
                else:
                    if(tmp_board[r+i][c+j] == '.'):
                        tmp_board[r+i][c+j] = char
                    else:
                        return False

    except IndexError:
        return False
    return tmp_board

def can_put(board, piece, r, c):
    for i, row in enumerate(piece):
        for j, char in enumerate(row):
            if(char != '.' and board[r+i][c+j] != '.'):
                return False
    return True

def no_copy_put(board, piece, r, c):
    if not can_put(board, piece, r, c):
        return False

    for i, row in enumerate(piece):
        for j, char in enumerate(row):
            if(char != '.'):
                board[r+i][c+j] = char

    return board

def cleanup(board, piece):
    piece_char = ''
    for i in piece[0]:
        if i != '.':
            piece_char = i
            break
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == piece_char:
                board[i][j] = '.'


def fill(board, r, c):
    if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
        if(board[r][c] == '.'):
            board[r][c] = 'X'
            return True
    return False

def debug(board, message=""):
    if message != "":
        print(message)
    pprint(board)
    input()

board = [
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
]

small_board = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]

small_b_pieces = [
e_piece,
d_piece,
n_piece,
c_piece,
l_piece,
m_piece
]
small_b_pieces_2 = [
a_piece,
b_piece,
f_piece,
g_piece,
h_piece,
o_piece
]

# new_board = put(board, a_piece[0], 1, 0)
# board = new_board

#pprint(board)
# pprint(put(board, b_piece[0], 0, 0))

def flood_fill_from(board, r, c):
    if(r<0 or c<0):
        return 0
    if fill(board, r, c) == False:
        return 0
    else:
        _r = flood_fill_from(board, r, c+1)
        _l = flood_fill_from(board, r, c-1)
        _u = flood_fill_from(board, r-1, c)
        _d = flood_fill_from(board, r+1, c)
        return 1 + _r + _l + _u + _d

def cleanup_flood_fill(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'X':
                board[r][c] = '.'

def in_losing_state(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '.':
                hole_size = flood_fill_from(board, r, c)
                # debug(test_board)
                if hole_size < 5 or hole_size % 5 != 0:
                    cleanup_flood_fill(board)
                    return True
    cleanup_flood_fill(board)
    return False

big_counter = 0
def benchmark():
    global big_counter
    big_counter += 1
    if big_counter % 10000 == 0:
        print(big_counter)

starting_positions = [0] * len(board)
def calculate_starting_positions(board):
    global starting_positions
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '.':
                starting_positions[r] = c
                break

def recursive_search(board, pieces, depth):
    if depth == len(pieces):
        # lock.acquire()
        # sol_ctr.value += 1
        # lock.release()
        # global t0
        # dt = (time.time_ns() - t0) / 1e9
        # print(f'Solutions: {sol_ctr.value}, time: {dt}, ({sol_ctr.value / dt} sol/sec)')
        pprint(board)
        return

    # if in_losing_state(board):
    #     return

    for p in pieces[depth]:
        for r in range(len(board) - len(p) + 1):
            for c in range(len(board[0]) - len(p[0]) + 1):
                # benchmark()
                new_board = no_copy_put(board, p, r, c)
                if new_board != False:
                    if in_losing_state(new_board):
                        cleanup(board, p)
                        continue
                    # debug(new_board)
                    # benchmark()
                    recursive_search(new_board, pieces, depth+1)
                    cleanup(board, p)

from multiprocessing import Process, Value, Lock
import os

mp_boards = []
for i in range(4):
    for j in range(2):
        mp_boards.append(put(board, a_piece[0], j, i))

processes = []
num_processes = os.cpu_count()
print(f"Number of CPU cores: {num_processes}\n")
# sol_ctr = Value('i', 0)
# lock = Lock()
# t0 = time.time_ns()

for i in range(num_processes):
    process = Process(target=recursive_search, args=(mp_boards[i], pieces, 0))
    processes.append(process)

for process in processes:
    process.start()

for process in processes:
    process.join()
