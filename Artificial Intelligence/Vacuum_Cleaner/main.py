
from room import Room
from normal_simple_reflex import normal_simple_reflex
from random_reflex_agent import random_simple_reflex
from random_reflex_agent_2 import random_simple_reflex_2
from model_based_reflex import model_based_reflex

if __name__ == "__main__":
    room_no_wall = Room()
    room_with_wall = Room()

    #setting walls (Best case)
    room_with_wall.set_wall(4,0,3)
    room_with_wall.set_wall(4,1,3)
    room_with_wall.set_wall(4,2,3)
    room_with_wall.set_wall(4,3,3)
    room_with_wall.set_wall(4,4,3)
    room_with_wall.set_wall(4,7,3)
    room_with_wall.set_wall(4,8,3)
    room_with_wall.set_wall(4,9,3)
    room_with_wall.set_wall(9,5,2)
    room_with_wall.set_wall(8,5,2)
    room_with_wall.set_wall(7,5,2)
    room_with_wall.set_wall(6,5,2)
    room_with_wall.set_wall(3,5,2)
    room_with_wall.set_wall(2,5,2)
    room_with_wall.set_wall(1,5,2)
    room_with_wall.set_wall(0,5,2)

    
    choice1=input("Select The Enviornmentt??:\n 1. Empty Room\n 2. 4 Rooms\n")
    if choice1=='1':
        room=room_no_wall
    elif choice1=='2':
        room=room_with_wall
    room.print_room()


    choice2=input("Select The Agent you want to implement??:\n 1. Simple deterministic\n 2. Random Simple\n 3. Memory-based\n 4. Random with changes\n")
    if choice2 == '2':
        random_simple_reflex(room)
    if choice2 =='1':
        normal_simple_reflex(room)
    if choice2 == '3':
        model_based_reflex(room)
    if choice2 == '4':
        random_simple_reflex_2(room)
    room.print_room()


