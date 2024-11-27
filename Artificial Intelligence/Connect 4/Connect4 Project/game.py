from ConnectState import ConnectState
from mcts import MCTS
from alphabeta import get_move
from heuristic import pick_best_move
from human import get_human_choice

def player(player, board, mcts = None, mcts_time = 0, minimax_depth = 0):
    choice = 0
    if(player == 1): 
        choice = get_human_choice()
    elif(player == 2):
        choice = pick_best_move(board)
    elif(player == 3):
        mcts.search(mcts_time)
        choice = mcts.best_move()
    elif(player == 4):
        choice = get_move(board, depth= minimax_depth)
    
    return choice
    

         

def play(player1, player2, mcts_time = 5, minimax_depth = 5):
    
    state = ConnectState()
    mcts1 = MCTS(state)
    mcts2 = MCTS(state)
    mcts_time = 5
    minimax_depth = 5
    steps = 0
    while not state.game_over():
        steps += 1
        print("Current state:")
        state.print()

        player1_move = player(player1, state.board, mcts = mcts1, mcts_time = mcts_time, minimax_depth = minimax_depth)

        state.move(player1_move)
        if(player2 == 3):
            mcts2.move(player1_move)

        state.print()

        if state.game_over():
            state.print()
            print("Player one won!")
            return 1, steps

        player2_move = player(player2, state.board, mcts = mcts2, mcts_time = mcts_time, minimax_depth = minimax_depth)


        state.move(player2_move)

        if(player1 == 3):
            mcts1.move(player2_move)


        if state.game_over():
            state.print()
            print("Player two won!")
            return 2, steps


# if __name__ == "__main__":
    # play()
