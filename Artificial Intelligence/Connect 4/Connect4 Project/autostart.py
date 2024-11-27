from game import play
from data import DataLogger
def main():
    options  = []
    for i in range(1, 6):
        options.append([2, 3, i, i])
    for i in range(1, 6):
        options.append([3, 2, i, i])
    for i in range(1, 6):
        options.append([2, 4, i, i])
    for i in range(1, 6):
        options.append([4, 2, i, i])


    logger = DataLogger()

    for p1, p2, mt, md in options:
        for i in range(10):
            winner, steps = play(p1, p2, mcts_time = mt, minimax_depth = md)
            logger.log(p1, p2, winner, steps, md, mt)
    
    print(logger.database)
    logger.get_csv()

            


if __name__== "__main__":
    main()