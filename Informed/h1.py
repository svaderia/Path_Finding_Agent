# Shyamal Vaderia : 2015A7PS0048P

from h_helper import *
from h_state import *
import random


def h1(root, goal_states):
    from collections import deque
    stack = deque()
    explored = set()
    stack.append(root)
    count = 1
    while len(stack) > 0:
        p = stack.pop()
        if p.state not in explored:
            if p.state.dirt_pos == []:
                return solution(p, goal_states)[::-1], p.path_cost, count
            explored.add(p.state)
            children = p.child_nodes()
            random.shuffle(children)
            children.sort(key = lambda x: x.score)
            for child in children:
                if child.state not in explored:
                    stack.append(child)
                    count+= 1             
    return -1 

def main():
    agent_pos = [1,2]
    dirt_pos = [[1,1],[2,2],[1,2],[4,2],[3,3],[5,5],[3,9],[2,8],[1,6],[8,6],[9,3],[5,7],[6,3]]
    mat_size = 10
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [9,9]
    goal_dirt_pos = []
    goal_state = [State(goal_agent_pos, goal_dirt_pos, mat_size)]
    root = HNode(initial_state, None, None, 0, 0, 0)
    print(gbs(root, goal_state))

if __name__ == "__main__":
    main()
