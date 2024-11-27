from game import play
def main():
    print("Connect 4")
    print("Select from the following options")
    player1 = int(input('''Select player 1:
    1. Human
    2. Heuristic
    3. MCTS
    4. Minimax
    
    Select: '''))
    player2 = int(input('''Select player 1:
    1. Human
    2. Heuristic
    3. MCTS
    4. Minimax

    Select: '''))
    mcts_time = 5
    minimax_depth = 5
    if (player1 == 3 or player2 == 3 or player1 == 1 or player2 == 1):
        mcts_time = int(input("Enter MCTS Time: "))
    if(player1 == 4 or player2 == 4):
        minimax_depth = int(input("Enter Minimax depth: "))

    winner, steps = play(player1, player2, mcts_time= mcts_time, minimax_depth=minimax_depth)
    





if __name__== "__main__":
    main()