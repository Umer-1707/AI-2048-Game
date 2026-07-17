import numpy as np
import random

def Initialize_Board():
    board = np.zeros((4, 4), dtype=int)
    board = spawn_new_tile(board)
    board = spawn_new_tile(board)
    return board

def spawn_new_tile(board):
    empty_position = get_empty_position(board)
    if not empty_position:
        return board
    i, j = random.choice(empty_position)
    tile_value = 4 if random.random() < 0.1 else 2
    board[i][j] = tile_value
    return board

def get_empty_position(board):
    empty = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty.append((i, j))
    return empty

def compress_n_merge(row):
    new_row = [num for num in row if num != 0]
    i = 0
    while i < len(new_row) - 1:
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
            i += 2
        else:
            i += 1
    new_row = [num for num in new_row if num != 0]
    while len(new_row) < 4:
        new_row.append(0)
    return new_row

def move_left(board):
    new_board = np.zeros((4, 4), dtype=int)
    for i in range(4):
        row = list(board[i])
        new_row = compress_n_merge(row)
        new_board[i] = new_row
    return new_board if not np.array_equal(board, new_board) else board

def reverse_rows(board):
    return np.array([row[::-1] for row in board])

def move_right(board):
    return reverse_rows(move_left(reverse_rows(board)))

def move_up(board):
    return move_left(board.T).T

def move_down(board):
    return reverse_rows(move_left(reverse_rows(board.T))).T

def make_move(board, direction):
    if direction == 'up': return move_up(board)
    elif direction == 'down': return move_down(board)
    elif direction == 'left': return move_left(board)
    elif direction == 'right': return move_right(board)
    else: raise ValueError(f"Invalid move direction: {direction}")

