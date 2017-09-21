# Shyamal Vaderia : 2015A7PS0048P

from bfs_helper import *
from bfs_state import *

def bfs(root, goal_states):
    from collections import deque
    frontier = deque()
    explored = set()
    frontier_check = set()
    frontier.append(root)
    frontier_check.add(root.state)
    count = 1 
    maxl = 1
    while len(frontier) > 0 :
        p = frontier.popleft()
        if len(frontier) > maxl:
            maxl = len(frontier)
        frontier_check.discard(p.state)
        if p.state in goal_states:
            return solution(p)[::-1], p.path_cost, count, maxl
        explored.add(p.state)
        for x in p.child_nodes():
            if x.state not in explored and x.state not in frontier_check:
                count += 1
                frontier_check.add(x.state)
                frontier.append(x)
    return -1

def main():
    agent_pos = [0,0]
    dirt_pos = [[1,1],[2,2],[1,2],[4,2],[3,3],[5,5],[3,9],[2,8],[1,6],[8,6],[9,3],[5,7],[6,3]]
    mat_size = 10
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [9,9]
    goal_dirt_pos = []
    goal_state = [State(goal_agent_pos, goal_dirt_pos, mat_size)]
    root = Node(initial_state, None, None, 0, 0)
    print(bfs(root, goal_state))

if __name__ == "__main__":
    main()
