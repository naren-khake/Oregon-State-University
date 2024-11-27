from agent import Agent
from plot_graph import Plot_graph
import random
import numpy as np
import matplotlib.pyplot as plot  


def random_simple_reflex(room, num_trials=50):
    multi = {'x': [0], 'y': [0], 'z' :[0]} 
    for i in range(num_trials):
        agent = Agent(room)
        count = 0
        while agent.is_running and agent.action_count < 10000:
            c = random.choice([1, 2, 3, 4])
            c3 = random.choice([1, 2, 3])

            if agent.sense_wall():
                if c3 == 2:
                    agent.turn_right()
                elif c3 == 1:
                    agent.turn_left()
                else:
                    agent.clean()
                continue

            if c == 1:
                agent.turn_right()
            elif c == 2:
                agent.turn_left()
            elif c == 3:
                agent.clean()
            else:
                agent.move_forward()
                count = 1

            if agent.sense_home() and count == 1:
                agent.turn_off()
                
        multi['x'].append(i)
        multi['y'].append(agent.action_count)
        multi['z'].append(agent.clean_tile)    
    #plot_graph = Plot_graph()
    #plot_graph.generate_graph(multi)

    #ploting x-y
    plot.plot(multi['x'], multi['y'], linestyle='-', color='orange')
    plot.xlabel('Number of Trial')
    plot.ylabel('Total Action Taken')
    plot.grid(True)
    plot.show()

    plot.plot(multi['x'], multi['z'], linestyle='-', color='b')
    plot.xlabel('Number of Trials')
    plot.ylabel('Total Tiles Cleaned')
    plot.grid(True)
    plot.show()

    plot.plot(multi['x'], np.mean(multi['y']), label='Average', color='orange', linestyle='--')
    plot.xlabel('Iteration')
    plot.ylabel('Average Cleaned Cells')
    plot.title('Average Number of Cleaned Cells Over 50 Runs')
    plot.legend()
    plot.show()

    print(f"Agent finished cleaning.\nTotal tiles cleaned: {agent.clean_tile}\nTotal action taken: {agent.action_count} ")
