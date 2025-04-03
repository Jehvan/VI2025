import math

from searching_framework import *

class Explorer(Problem):
    def __init__(self, initial, golemina,dzidovi,house, goal=None):
        super().__init__(initial, goal)
        self.goal = goal
        self.size = golemina
        self.walls = tuple(dzidovi)
        self.house = house

    def successor(self, state):
        covek = state
        successors = dict()
        moves = {
            "Gore":(0,1),
            "Dolu":(0,-1),
            "Levo":(-1,0),
            "Desno":(1,0),
            "Desno 2":(2,0),
            "Desno 3":(3,0)
        }

        for move in moves:
            dvizenje = moves[move]
            new_covek = covek[:]
            new_x, new_y = new_covek[0] + dvizenje[0], new_covek[1] + dvizenje[1]
            if 0 <= new_x < self.size and 0 <= new_y < self.size and (new_x, new_y) not in self.walls:
                if move == "Desno 2":
                    if (new_covek[0] + 1, new_y) not in self.walls:
                        successors[move] = (new_x, new_y)
                elif move == "Desno 3":
                    if (new_covek[0] + 1, new_y) not in self.walls and (new_covek[0] + 2, new_y) not in self.walls:
                        successors[move] = (new_x, new_y)
                else:
                    successors[move] = (new_x, new_y)

        return successors

    def h(self,node):
        state = node.state
        covekx = state[0]
        coveky = state[1]
        kukjax = self.house[0]
        kukjay = self.house[1]

        manhattan_distance = abs(covekx - kukjax) + abs(coveky - kukjay)

        return math.ceil(manhattan_distance / 3)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.house[0] and state[1] == self.house[1]


if __name__ == '__main__':
    size = int(input())
    n = int(input())
    walls =[]
    for i in range(n):
        wall = input().split(",")
        wall[0] = int(wall[0])
        wall[1] = int(wall[1])
        walls.append((wall[0],wall[1]))
    input_covece = input().split(",")
    covece = tuple((int(input_covece[0]), int(input_covece[1])))
    input_kuka = input().split(",")
    kuka = tuple((int(input_kuka[0]), int(input_kuka[1])))
    explorer = Explorer(covece,size,walls,kuka)
    result = astar_search(explorer, explorer.h)
    if result is not None:
        print(result.solution())


