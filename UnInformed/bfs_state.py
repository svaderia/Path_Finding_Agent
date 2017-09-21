# Shyamal Vaderia : 2015A7PS0048P

class State:

    def __init__(self, agent_pos, dirt_pos, mat_size):
        """
        agent_pos: coordinate of agent's postition
        dirt_pos: a list containing all the positions of the dirt
        """
        self.agent_pos = agent_pos
        self.dirt_pos = dirt_pos
        self.mat_size = mat_size

    def __eq__(self, other):
        return (self.agent_pos == other.agent_pos and self.dirt_pos == other.dirt_pos)

    def __hash__(self):
        return hash((tuple(self.agent_pos), tuple([tuple(x) for x in self.dirt_pos])))


class Node:

    def __init__(self, state, parent, action, path_cost, depth):
        """
        state: the state in the state space to which the node corresponds.
        parent: the node on the search tree that generated this node.
        action: the action that was applied to the parent to generate the node
        path_cost: the cost of the path from the initial state to the node, as indicated by the parent pointers
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

    def __str__(self):
        return "action: {} \t cost: {} \t pos: [{},{}] \t dirt: {}".format(self.action, self.path_cost, self.state.agent_pos[0], self.state.agent_pos[1], self.state.dirt_pos)

    def _getx(self):
        return self.state.agent_pos[0]
    
    def _gety(self):
        return self.state.agent_pos[1]

    def child_nodes(self):
        childs = []
        indx = self.state.dirt_pos.index(self.state.agent_pos) if self.state.agent_pos in self.state.dirt_pos else -1
        parent = self
        
        if self.state.dirt_pos is not None and indx != -1:
            action = "suck"
            path_cost = self.path_cost + 1
            new_dirt_pos = self.state.dirt_pos[:indx] + self.state.dirt_pos[indx+1:]
            state = State([x for x in self.state.agent_pos], new_dirt_pos, self.state.mat_size)
            newchild = Node(state, parent, action, path_cost, self.depth + 1)
            childs.append(newchild)
        else:
            up = self._getx() > 0
            down = self._getx() < self.state.mat_size - 1
            right = self._gety() <  self.state.mat_size - 1
            left = self._gety() > 0
            
            path_cost = self.path_cost + 2
            
            if up:
                action = "up"
                state = State([self._getx()-1 , self._gety()], self.state.dirt_pos, self.state.mat_size)
                newchild = Node(state, parent, action, path_cost, self.depth + 1)
                childs.append(newchild)
            if left:
                action = "left"
                state = State([self._getx(), self._gety()-1], self.state.dirt_pos, self.state.mat_size)
                newchild = Node(state, parent, action, path_cost, self.depth + 1)
                childs.append(newchild)
            if right:
                action = "right"
                state = State([self._getx(), self._gety()+1], self.state.dirt_pos, self.state.mat_size)
                newchild = Node(state, parent, action, path_cost, self.depth + 1)
                childs.append(newchild)
            if down:
                action = "down"
                state = State([self._getx()+1, self._gety()], self.state.dirt_pos, self.state.mat_size)
                newchild = Node(state, parent, action, path_cost, self.depth + 1)
                childs.append(newchild)
        return childs


def main():
    pass

if __name__ == "__main__":
    main()
