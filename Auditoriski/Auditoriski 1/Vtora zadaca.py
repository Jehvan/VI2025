from searching_framework import Problem
from searching_framework.uninformed_search import *

class Explorer(Problem):
    def __init__(self,initial,goal = None):
        super().__init__(initial,goal)
        self.size = [8,6]

    def successor(self, state):
        # d = -1 (nadolu)
        # d = 1 (nagore)
        # (x,y, (x_01,, y_01, d_01), (x_02,y_02,d_02))
        man_x = state[0]
        man_y = state[1]

        obstacle1 = list(state[2])
        obstacle2 = list(state[3])

        if obstacle1[2] == 1: #up
            if obstacle1[1] == self.size[1] - 1:
                obstacle1[1] = -1
                obstacle1[1] -= 1
            else:
                obstacle1[1] += 1
        else: #down
            if obstacle1[1] == 0:
                obstacle1[2] = -1
                obstacle1[1] += 1
            else:
                obstacle1[1] -= 1
        if obstacle2[2] == 1: #up
            if obstacle2[1] == self.size[1] - 1:
                obstacle2[1] = -1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else: #down
            if obstacle2[1] == 0:
                obstacle2[2] = -1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles = [(obstacle1[0],obstacle1[1]),(obstacle2[0],obstacle2[1])]
        successors = dict()
        # right x = x + 1
        if man_x + 1 < self.size[0] and (man_x + 1,man_y) not in obstacles:
            successors["Right"] = (man_x + 1, man_y, (obstacle1[0],obstacle1[1],obstacle2[2]),(obstacle2[0],obstacle2[1],obstacle2[2]))
        # left x = x - 1
        if man_x - 1 > 0 and (man_x - 1, man_y) not in obstacles:
            successors["Left"] = (man_x - 1, man_y, (obstacle1[0], obstacle1[1], obstacle2[2]), (obstacle2[0], obstacle2[1], obstacle2[2]))
        # up y = y + 1
        if man_y + 1 < self.size[1] and (man_x, man_y + 1) not in obstacles:
            successors["Up"] = (man_x, man_y + 1, (obstacle1[0], obstacle1[1], obstacle2[2]), (obstacle2[0], obstacle2[1], obstacle2[2]))
        #down y = y - 1
        if man_y - 1 > 0 and (man_x, man_y - 1) not in obstacles:
            successors["Down"] = (man_x, man_y - 1, (obstacle1[0], obstacle1[1], obstacle2[2]), (obstacle2[0], obstacle2[1], obstacle2[2]))
        return successors
    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

if __name__ == '__main__':
    goal_state = (7,4)
    initial_state = (0,2)
    obstacle1 = (2,5,-1)
    obstacle2 = (5,0,1)

    explorer = Explorer((initial_state[0],initial_state[1],obstacle1,obstacle2),goal_state)
    print(breadth_first_graph_search(explorer).solution())