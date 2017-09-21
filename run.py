# Shyamal Vaderia : 2015A7PS0048P

import sys
from time import time
from Gui.gui import *
from UnInformed.bfs import bfs
from UnInformed.ids import *
from UnInformed.bfs_state import *
from Informed.h1 import *
from Informed.h2 import *
from Informed.h_state import HNode

def option_1():
    screen , t, grid_1, grid_2, screen_width, screen_height, xcord, dirt_list = Screen_init()
    agent_pos = [0,0]
    mat_size = 10
    dirt_pos = [[x[1],x[0]] for x in dirt_list]
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [[9,9], [0,0], [0,9], [9,0]]
    goal_dirt_pos = []
    goal_states = []
    for pos in goal_agent_pos:
        goal_states.append(State(pos, goal_dirt_pos, mat_size))

def option_2():
    percentage = input("Enter the percentage of dirt: ")
    agent_pos = [0,0]
    mat_size = 10
    coord = [[i,j] for i in range(mat_size) for j in range(mat_size)]
    coord.remove([0,0])
    coord.remove([0,9])
    coord.remove([9,0])
    coord.remove([9,9])
    num = mat_size**2*percentage//100
    lst = random.sample(coord, num)
    dirt_pos = [[x[1],x[0]] for x in lst]
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [[9,9], [0,0], [0,9], [9,0]]
    goal_dirt_pos = []
    goal_states = []
    for pos in goal_agent_pos:
        goal_states.append(State(pos, goal_dirt_pos, mat_size))
    idst = time()
    root = Node(initial_state, None, None, 0, 0)
    action_path = ids(root, goal_states)
    print(action_path[0])
    print("Path Cost : " + str(action_path[1]))

def option_3():
    percentage = input("Enter the percentage of dirt: ")
    agent_pos = [0,0]
    mat_size = 10
    coord = [[i,j] for i in range(mat_size) for j in range(mat_size)]
    coord.remove([0,0])
    coord.remove([0,9])
    coord.remove([9,0])
    coord.remove([9,9])
    num = mat_size**2*percentage//100
    lst = random.sample(coord, num)
    dirt_pos = [[x[1],x[0]] for x in lst]
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [[9,9], [0,0], [0,9], [9,0]]
    goal_dirt_pos = []
    goal_states = []
    for pos in goal_agent_pos:
        goal_states.append(State(pos, goal_dirt_pos, mat_size))
    idst = time()
    root = HNode(initial_state, None, None, 0, 0,0,0)
    action_path = h1(root, goal_states)
    print(action_path[0])
    print("Path Cost By H1 : " + str(action_path[1]))
    action_path = h2(root, goal_states)
    print(action_path[0])
    print("Path Cost By H2 : " + str(action_path[1]))
    

def main():
    screen , t, grid_1, grid_2, screen_width, screen_height, xcord, dirt_list = Screen_init()
    agent_pos = [0,0]
    mat_size = 10
    dirt_pos = [[x[1],x[0]] for x in dirt_list]
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [[9,9], [0,0], [0,9], [9,0]]
    goal_dirt_pos = []
    goal_states = []
    for pos in goal_agent_pos:
        goal_states.append(State(pos, goal_dirt_pos, mat_size))
    # H1
    th1 = time()
    root2 = HNode(initial_state, None, None, 0, 0, 0, 0)
    sz = sys.getsizeof(HNode)
    action_path = h1(root2, goal_states)
    th1 = round(time() - th1, 4)
    print(action_path, th1)
    trace_path(action_path[0], grid_2, screen_width, screen_height,1)
    # Rs
    writer(6 ,"{} Nodes".format(action_path[2]),screen,t,xcord,1)
    writer(7 ,"{} KBytes".format(sz),screen,t,xcord,1)
    writer(8 ,"{} Cost".format(action_path[1]),screen,t,xcord,1)
    writer(9 ,"{} Seconds".format(th1),screen,t,xcord,1)
    
    # H2
    th2 = time()
    root2 = HNode(initial_state, None, None, 0, 0, 0, 0)
    sz = sys.getsizeof(HNode)
    action_path = h2(root2, goal_states)
    th2 = round(time() - th2, 4)
    print(action_path, th2)
    trace_path(action_path[0], grid_2, screen_width, screen_height,2)
    # Rs
    writer(6.5 ,"{} Nodes".format(action_path[2]),screen,t,xcord,2)
    writer(7.5 ,"{} KBytes".format(sz),screen,t,xcord,2)
    writer(8.5 ,"{} Cost".format(action_path[1]),screen,t,xcord,2)
    writer(9.5 ,"{} Seconds".format(th2),screen,t,xcord,2)
    
    # IDS
    idst = time()
    root = Node(initial_state, None, None, 0, 0)
    ids_sz = sys.getsizeof(Node)
    ids_action_path = bfs(root, goal_states)
    idst = round(time() - idst, 4)
    print(ids_action_path)
    trace_path(ids_action_path[0], grid_1, screen_width, screen_height,0)
    # Rs
    writer(1 ,"{} Nodes".format(ids_action_path[2]),screen,t,xcord,0)
    writer(2 ,"{} KBytes".format(ids_sz),screen,t,xcord,0)
    writer(3 ,"{} Max Growth".format(ids_action_path[3]),screen,t,xcord,0)
    writer(4 ,"{} Cost".format(ids_action_path[1]),screen,t,xcord,0)
    writer(5 ,"{} Seconds".format(idst),screen,t,xcord,0)
    
    mem_diff = ids_action_path[2]*ids_sz - action_path[2]*sz
    writer(10 ,"{} KBytes".format(mem_diff),screen,t,xcord,0)
    writer(10.5 ,"Memory Difference",screen,t,xcord,0)

    
    agent_pos = [0,0]
    mat_size = 5
    percentage = 30
    coord = [[i,j] for i in range(mat_size) for j in range(mat_size)]
    num = mat_size**2*percentage//100
    dirt_list = random.sample(coord, num)
    dirt_pos = [[x[1],x[0]] for x in dirt_list]
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [[4,4], [0,0], [0,4], [4,0]]
    goal_dirt_pos = []
    goal_states = []
    
    for pos in goal_agent_pos:
        goal_states.append(State(pos, goal_dirt_pos, mat_size))
    root = Node(initial_state, None, None, 0, 0)
    root2 = HNode(initial_state, None, None, 0, 0, 0, 0)
    path_cost_1 = 0
    path_cost_2 = 0
    for _ in range(10):
        path_cost_1 += h2(root2, goal_states)[1]
        path_cost_2 += bfs(root2, goal_states)[1]
    writer(11 ,"{} Avg. Cost".format(path_cost_2/10),screen,t,xcord,0)
    writer(11.5 ,"{} Avg. Cost".format(path_cost_1/10),screen,t,xcord,2)
    
    ##############################################################
    # G3
    time_h1 = []
    time_h2 = []
    percentage = 30
    for mat_size in range(3, 15):
        agent_pos = [0,0]
        coord = [[i,j] for i in range(mat_size) for j in range(mat_size)]
        num = mat_size**2*percentage//100
        dirt_pos = random.sample(coord, num)
        initial_state = State(agent_pos, dirt_pos, mat_size)
        goal_agent_pos = [[0,0]]
        goal_dirt_pos = []
        goal_states = [State(pos, goal_dirt_pos, mat_size)]
        root = HNode(initial_state, None, None, 0, 0, 0, 0)
        t0 = time()
        temp = h1(root, goal_states)
        t1 = round(time() - t0, 4)
        time_h1.append(t1)
        t2 = time()
        temp = h2(root, goal_states)
        t3 = round(time() - t2, 4)
        time_h2.append(t3)

    max1 = max(time_h1)
    max2 = max(time_h2)
    min1 = min(time_h1)
    min2 = min(time_h2)

    n_t_h1 = []
    n_t_h2 = []
    for i in time_h1:
        n_t_h1.append((i - min1)/(max1 - min1) * (screen_height - 100)/2)
    print(n_t_h1)
    for i in time_h2:
        n_t_h2.append((i - min2)/(max2 - min2) * (screen_height - 100)/2)
    print(n_t_h2)

    t = Turtle()
    t.pensize(2)
    t.penup()
    t.setpos((screen_width/3)-(screen_width/2) + 30, (-1 * (screen_height- 50))/2)
    t.pendown()
    t.setheading(0)
    t.fd(screen_width/3 - 60)
    t.setheading(90)
    t.penup()
    t.setpos((screen_width/3)-(screen_width/2)+30, (-1 * (screen_height- 50))/2)
    t.pendown()
    t.fd((screen_height - 100)/2)
    t.penup()
    t.setpos((screen_width/3)-(screen_width/2)+30, (-1 * (screen_height- 50))/2)
    t.pendown()

    k = 1
    t.pensize(1.5)
    t.pencolor("green")
    for i in n_t_h1:
        t.setpos((screen_width/3) - (screen_width/2) + 30 + ((screen_width-60)/3)*k/14, (-1*(screen_height-100)/2) + i)
        k += 1

    k = 1
    t.pencolor("orange")
    t.penup()
    t.setpos((screen_width/3)-(screen_width/2)+30, (-1 * (screen_height- 50))/2)
    t.pendown()
    for i in n_t_h2:
        t.setpos((screen_width/3) - (screen_width/2) + 30 + ((screen_width-60)/3)*k/14, (-1*(screen_height-100)/2) + i)
        k += 1
    ##################################################################################
    # G4
    time_list = []
    mat_size = 10
    for percentage in range(10, 105, 5):
        agent_pos = [0,0]
        coord = [[i,j] for i in range(mat_size) for j in range(mat_size)]
        num = mat_size**2*percentage//100
        dirt_pos = random.sample(coord, num)
        initial_state = State(agent_pos, dirt_pos, mat_size)
        goal_agent_pos = [[0,0]]
        goal_dirt_pos = []
        goal_states = [State(pos, goal_dirt_pos, mat_size)]
        root = HNode(initial_state, None, None, 0, 0, 0, 0)
        t0 = time()
        temp = h1(root, goal_states)
        # action_list = temp[0][0]
        # trace_path(action_list, coordinates_1, width, height)
        t1 = round(time() - t0, 4)
        time_list.append(t1)

    maxt = max(time_list)
    mint = min(time_list)
    new_time_list = []
    for time_instance in time_list:
        new_time_list.append((time_instance - mint)/(maxt - mint) * (screen_height - 100)/2)

    t.pencolor("black")
    t.pensize(2)
    t.penup()
    t.setpos(-1*((screen_width/3)-(screen_width/2)) + 30, (-1 * (screen_height- 50))/2)
    t.pendown()
    t.setheading(0)
    t.fd(screen_width/3 - 60)
    t.setheading(90)
    t.penup()
    t.setpos(-1*((screen_width/3)-(screen_width/2))+30, (-1 * (screen_height- 50))/2)
    t.pendown()
    t.fd((screen_height - 100)/2)
    t.penup()
    t.setpos(-1*((screen_width/3)-(screen_width/2))+30, (-1 * (screen_height- 50))/2)
    t.pendown()

    c = 10
    t.pensize(2)
    t.pencolor("cyan3")
    for i in new_time_list:
        t.setpos(-1*((screen_width/3)-(screen_width/2))+30 + ((screen_width-90)/3)*c/110, (-1 * (screen_height - 100)/2) + i)
        c += 5
    t.ht()
    
    exitonclick()

if __name__ == "__main__":
    a = \
"""
Option 1: Display the room environment
Option 2: Find the path (action sequence) and path cost using T1
Option 3: Find the path (action sequence) and path cost using T2
Option 4: Show all results and graphs in the GUI.
"""
    print(a)
    a = int(input("Enter the number between 1-4 to choose any of the above option "))
    if a == 1:
        option_1()
        exitonclick()
    elif a == 2:
        option_2()
    elif a == 3:
        option_3()
    elif a == 4:
        main()
    else:
        print("Please enter a valid number next time")