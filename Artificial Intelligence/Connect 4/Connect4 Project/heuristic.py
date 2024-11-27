import random
from alphabeta import get_valid_locations, get_next_open_row, evaluate_window, score_position, drop_piece

def pick_best_move(board):
    # print(board)
    piece = 2
    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
            
    return best_col
