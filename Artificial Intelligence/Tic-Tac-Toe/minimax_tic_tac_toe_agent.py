# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Naren Digambar Khake


class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

    def action(self, state):
        if state==('X', None, None, None, None, None, None, None, None):
            return None
        else:
            return self.minimax(self.game,state)

    def minimax(self, game, state):
        """"
        Objective: Calculate the optimal action for the current player using the minimax algorithm.

        Arguments: game: The game object representing the Tic-Tac-Toe game from tic_tac_toe_game.py.
                   state: The current state of the game.
         Returns:  int value: The optimal action for the current player in the given state.
        """

        game.player=game.to_move(state)
        value,move= self.max_value(game,state)
        print("move")
        return move

    def max_value(self, game, state):
        """
        Objective: Calculate the maximum value achievable by the current player in the given state using the minimax algorithm.
        
        Arguments:  game : The game object representing the Tic-Tac-Toe game from tic_tac_toe_game.py.
                    state : The current state of the game.

        Returns:  A maximum utility value and the corresponding action.
        """
        if game.is_terminal(state):
            return game.utility(state,game.player),None
        v = -float('inf')
        for a in game.actions(state):
            v2,a2=self.min_value(game,game.result(state,a))
            if v2>v:
                v,move=v2,a
        return v,move
            

    def min_value(self, game, state):
        """
        Objective:  Calculate the minimum value achievable by the current player in the given state using the minimax algorithm.
        Arguments:  game : The game object representing the Tic-Tac-Toe game from tic_tac_toe_game.py.
                    state : The current state of the game.

        Returns:  A minimum utility value and the corresponding action.
        """
        if game.is_terminal(state):
            return game.utility(state,game.player),None
        v = float('inf')
        for a in game.actions(state):
            v2,a2=self.max_value(game,game.result(state,a))
            if v2<v:
                v,move=v2,a
        return v,move
