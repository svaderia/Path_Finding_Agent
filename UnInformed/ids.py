# Shyamal Vaderia : 2015A7PS0048P

from time import time
from bfs_helper import *
from bfs_state import *

# def dls(root, goal_state, depth):
#     if root.state == goal_state:
#         return solution(root) 
#     if depth == 0:
#         return "cutoff"
#     for x in root.child_nodes():
#         ct = False
#         result = dls(x, goal_state, depth - 1)
#         if result == "cutoff":
#             ct = True
#         if result != -1: return result
#     if ct: return "cutoff"
#     else: return -1

# def dls2(root, goal_state, depth):
#     from collections import deque
#     stack = deque()
#     stack.append((root, 0))
#     # explored = set()
#     while len(stack) > 0:
#         p = stack.pop()
#         if p[0].state in goal_state:
#             return solution(p[0])[::-1],p[0].path_cost
#         # explored.add(p[0].state)
#         if p[1] < depth:
#             for x in p[0].child_nodes():
#                 # if x.state not in explored:
#                     stack.append((x, p[1]+1))
#     return -1

# def dls3(root, goal_state, depth):
#     from collections import deque
#     stack = deque()
#     stack.append(root)
#     explored = set()
#     while len(stack) > 0 :
#         p = stack.pop()
#         if p.state in goal_state:
#             return solution(p)[::-1], p.path_cost, p.depth
#         explored.add(p.state)
#         if p.depth < depth:
#             for child in p.child_nodes():
#                 if child.state not in explored:
#                     stack.append(child)
#         else:
#             explored = set()
#     return -1

def dls(root, goal_state, depth, explored):
    from collections import deque
    stack = deque()
    stack.append(root)
    count = 1
    maxl = 1
    while len(stack) > 0 :
        if len(stack) > maxl:
            maxl = len(stack)
        p = stack.pop()
        if p.state in goal_state:
            return solution(p)[::-1], p.path_cost, count, maxl
        if p.depth < depth:
            for child in p.child_nodes():
                if child.state not in explored:
                    explored[child.state] = child.path_cost
                    count += 1
                    stack.append(child)
                else:
                    if explored[child.state] >= child.path_cost:
                        explored[child.state] = child.path_cost
                        stack.append(child)
                        count += 1
    return -1

# def ids(root, goal_state):
#     i = 1
#     while True:
#         res = dls3(root, goal_state, i)
#         print(i)
#         if res != -1:
#             return res
#         i += 1

def ids(root, goal_state):
    i = 1
    explored = {}
    explored[root.state] = 0
    while True:
        res = dls(root, goal_state, i, explored)
        print("Depth: {}".format(i))
        if res != -1:
            return res
        i += 1

def main():
    agent_pos = [0,0]
    dirt_pos = [[1,1],[2,2],[1,2],[4,2],[3,3],[5,5],[3,9],[2,8],[1,6],[8,6],[9,3],[5,7],[6,3]]
    mat_size = 10
    initial_state = State(agent_pos, dirt_pos, mat_size)
    goal_agent_pos = [9,9]
    goal_dirt_pos = []
    goal_state = [State(goal_agent_pos, goal_dirt_pos, mat_size)]
    root = Node(initial_state, None, None, 0, 0)
    print(ids2(root, goal_state))

    

if __name__ == "__main__":
    main()
