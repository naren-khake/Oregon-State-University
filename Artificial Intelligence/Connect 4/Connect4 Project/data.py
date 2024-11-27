import pandas as pd

class DataLogger:
    algo_mapper = {1:"human", 2:"heuristic", 3:"mcts", 4:"minimax"}
    def __init__(self):
        self.columns = ["algo1", "algo2", "winner", "steps", "minimax_depth", "mcts_time"]
        self.database = []

    def log(self, algorithm1, algorithm2, winner, steps, minimax_depth, mcts_time):
        obj = self.get_obj(algorithm1, algorithm2, winner, steps, minimax_depth, mcts_time)
        self.database.append(obj)

    def get_obj(self, algorithm1, algorithm2, winner, steps, minimax_depth, mcts_time):
        return {
                "algo1": self.algo_mapper[algorithm1],
                "algo2": self.algo_mapper[algorithm2],
                "winner": winner,
                "steps": steps,
                "minimax_depth": minimax_depth,
                "mcts_time": mcts_time
                }

    def get_csv(self):
        df = pd.DataFrame.from_dict(self.database)
        print(df)
        df.to_csv("games_data.csv", index=False)
    