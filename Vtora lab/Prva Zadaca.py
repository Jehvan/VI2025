import math

from searching_framework import *
size = (5,9)



class Explorer(Problem):
    def __init__(self, initial,zeleni, goal = None):
        super().__init__(initial,goal)
        self.grid_size = size
        self.zeleni = zeleni

    def successor(self,state):
        successors = dict()
        man_x, man_y = state[0][0],state[0][1]
        kukja = state[1]
        kukja = list(kukja)
        if kukja[2] == 'desno' and kukja[0] != 4:
            kukja[0] = kukja[0] + 1
        elif kukja[2] == 'desno' and kukja[0] == 4:
            kukja[0] = kukja[0] - 1
            kukja[2] = 'levo'
        elif kukja[2] == 'levo' and kukja[0] != 0:
            kukja[0] = kukja[0] - 1
        elif kukja[2] == 'levo' and kukja[0] == 0:
            kukja[0] = kukja[0] + 1
            kukja[2] = 'desno'

        moves = {
            "Stoj":(0,0),
            "Gore 1":(0,1),
            "Gore 2":(0,2),
            "Gore-desno 1":(1,1),
            "Gore-desno 2":(2,2),
            "Gore-levo 1":(-1,1),
            "Gore-levo 2":(-2,2)
        }
        for move in moves:
            direction = moves[move]
            new_x = state[0][0] + direction[0]
            new_y = state[0][1] + direction[1]
            if(0 <= new_x < size[0] and 0 <= new_y < size[1]) and ((new_x, new_y) in self.zeleni or (new_x == kukja[0] and new_y == kukja[1])):
                successors[move] = ((new_x,new_y),tuple(kukja))
        return successors

    def h(self,node):
        covekx = node.state[0][0]
        coveky = node.state[0][1]
        kukjax = node.state[1][0]
        kukjay = node.state[1][1]
        distance = math.floor(math.sqrt((covekx-kukjax)**2 + (coveky-kukjay)**2)/2)
        return distance
    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0][0] == state[1][0] and state[0][1] == state[1][1]

if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    # your code here
    #x,y
    vlez_covece = input().split(',')
    covece = (int(vlez_covece[0]), int(vlez_covece[1]))
    #x,y,nasoka
    vlez = input().split(',')
    vlez_kuka_x = vlez[0]
    vlez_kuka_y = vlez[1]
    vlez_nasoka = input()
    kuka = (int(vlez_kuka_x), int(vlez_kuka_y),vlez_nasoka)
    explorer = Explorer ((covece,kuka), allowed)

    rez = astar_search(explorer,explorer.h)
    if rez is not None:
        print(rez.solution())
    else: print("a")