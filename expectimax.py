from board import make_move, get_empty_position
import numpy as np

def get_valid_moves(board):
    directions = ['up', 'down', 'left', 'right']
    return [d for d in directions if not np.array_equal(make_move(board, d), board)]

def heuristic_score(board):
    empty_cells = len(get_empty_position(board))
    max_tile = np.max(board)

    empty_score = empty_cells * 100

    corners = [board[0][0], board[0][3], board[3][0], board[3][3]]
    corner_bonus = max_tile * 3 if max_tile in corners else 0

    mono_score = 0
    for row in board:
        for i in range(3):
            if row[i] >= row[i+1]:
                mono_score += row[i]
    for col in board.T:
        for i in range(3):
            if col[i] >= col[i+1]:
                mono_score += col[i]

    smoothness = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                for dx, dy in [(0,1), (1,0)]:
                    x, y = i+dx, j+dy
                    if x < 4 and y < 4 and board[x][y] != 0:
                        smoothness -= abs(board[i][j] - board[x][y])

    return empty_score + mono_score + corner_bonus + smoothness

def expectimax(board, depth, is_ai_turn):
    if depth == 0 or not get_valid_moves(board):
        return heuristic_score(board)

    if is_ai_turn:
        return max(expectimax(make_move(np.copy(board), move), depth-1, False)
                   for move in get_valid_moves(board))
    else:
        empty = get_empty_position(board)
        expected_score = 0
        for (i, j) in empty:
            for value, prob in [(2, 0.9), (4, 0.1)]:
                new_board = np.copy(board)
                new_board[i][j] = value
                expected_score += prob * expectimax(new_board, depth-1, True) / len(empty)
        return expected_score

def get_best_move(board, depth=3):
    best_score = float('-inf')
    best_move = None
    for move in get_valid_moves(board):
        score = expectimax(make_move(np.copy(board), move), depth-1, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

