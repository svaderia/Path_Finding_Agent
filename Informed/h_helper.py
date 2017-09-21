# Shyamal Vaderia : 2015A7PS0048P


import random
def solution(root, goal_state):
    seq = list()
    agent_state = root.state.agent_pos
    goal_list = [x.agent_pos for x in goal_state]
    if agent_state not in goal_list:
        fin_state = dist(agent_state, goal_list)
        wid = "left" if agent_state[1] - fin_state[1] > 0 else "right"
        hg = "up" if agent_state[0] - fin_state[0] > 0 else "down"
        lst = [wid]*abs(agent_state[1] - fin_state[1]) + [hg]*abs(agent_state[0] - fin_state[0])
        seq.extend(lst)
    while root.parent != None:
        seq.append(root.action)
        root = root.parent
    
    return seq

def dist(pos, goal_list):
    return min([(sum(abs(x - y) for x,y in zip(pos,gs)), gs) for gs in goal_list], key= lambda x : x[0])[1]

def main():
    a = [4,4]
    b = [[0,0],[9,9],[0,9],[9,0]]
    print(dist(a,b))

if __name__ == "__main__":
    main()
