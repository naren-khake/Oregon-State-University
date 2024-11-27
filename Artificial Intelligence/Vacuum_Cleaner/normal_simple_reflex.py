from agent import Agent
from plot_graph import Plot_graph


def normal_simple_reflex(room):
    agent = Agent(room)
    graph = Plot_graph()
    count=0
    while agent.is_running and agent.action_count<5000:
        if agent.sense_wall():
            if agent.sense_dirt():
                agent.turn_right()
            else:
                agent.turn_left()
            continue
        if agent.sense_dirt():
            agent.clean()
            continue
        if agent.sense_home() and count==1:
            agent.turn_off()
            continue
        agent.move_forward()
        count=1
    gp=agent.graph
    plot_graph=Plot_graph()
    plot_graph.generate_graph(gp)
    print(f"Agent finished cleaning.\ntotal tiles cleaned :{agent.clean_tile} \n Total action taken: {agent.action_count} ")
    