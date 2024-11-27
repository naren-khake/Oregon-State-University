from agent import Agent
from plot_graph import Plot_graph

def model_based_reflex(room):
    agent = Agent(room)
    graph = Plot_graph()
    state=[0,0,0]
    count=0
    while agent.is_running and agent.action_count<10000:
        if agent.sense_wall():
            if agent.sense_dirt():
                if state[1]==2:
                    agent.turn_left()
                    state[2]+=1
                    state[1]=0
                else:
                    agent.turn_right()
                    state[1]+=1
                    state[2]=0
            else:
                if state[2]==0:
                    agent.turn_left()
                    state[1]=0
                    state[2]=0
                else:
                    agent.turn_right()
                    state[1]=0
                    state[2]=0
            continue

        if agent.sense_dirt():
            agent.clean()

        if agent.sense_home() and count==1:
            agent.turn_off()
            continue
        agent.move_forward()

        if state[1]==1:
            agent.turn_right()
            state[1]+=1
        elif state[2]==1:
            agent.turn_left()
            state[2]+=1
        count=1
    gp=agent.graph
    plot_graph=Plot_graph()
    plot_graph.generate_graph(gp)
    print(f"Agent finished cleaning.\ntotal tiles cleaned :{agent.clean_tile} \n Total action taken: {agent.action_count} ")
