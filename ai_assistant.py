from board import Initialize_Board, make_move, spawn_new_tile
from expectimax import get_best_move , get_valid_moves
import numpy as np

key_to_direction = {
    'u': 'up',
    'l': 'left',
    'd': 'down',
    'r': 'right'
}

def play_with_ai_assistant():
    board = Initialize_Board()

    while True:
        print("\nCurrent board:")
        print(board)

        suggestion = get_best_move(board, depth=3)
        print(f"\n🤖 AI Suggestion: {suggestion.upper()}")

        move = input("Your move (U/L/D/R or Q to quit): ").lower()
        if move == 'q':
            print("Game exited.")
            break

        if move not in key_to_direction:
            print("Invalid input! Use U/L/D/R.")
            continue

        direction = key_to_direction[move]
        new_board = make_move(np.copy(board), direction)

        if np.array_equal(new_board, board):
            print("⚠️ Invalid move. Try another direction.")
            continue

        board = spawn_new_tile(new_board)

        if not get_valid_moves(board):
            print("\n💀 Game Over!")
            print(board)
            break

