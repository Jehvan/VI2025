from searching_framework import *


# from utils import *
# from uninformed_search import *
# from informed_search import *

def around_box(covek,box):
    niza = []
    for box_1 in box:
        if max(abs(covek[0] - box_1[0]), abs(covek[1] - box_1[1])) <= 1:
            niza += (box_1,)
    return niza

class Boxes(Problem):
    def __init__(self, initial,n,kutii, goal=None):
        super().__init__(initial, goal)
        self.n = n
        self.kutii = kutii

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0


    def successor(self, state):
        successors = dict()
        moves = {
            "Gore":(0,1),
            "Desno":(1,0)
        }
        n = self.n
        covek = state[0]
        for move in moves:
            boxes_ = (state[1])[:]
            direction = moves[move]
            newx,newy = covek[0] + direction[0], covek[1] + direction[1]
            new_covek = (newx,newy)
            if 0 <= newx < n and 0 <= newy < n and new_covek not in self.kutii:
                if boxes_ and around_box(new_covek,boxes_):
                    niza = around_box(new_covek, boxes_)
                    for box in niza:
                        # niza = [tuple(s) for s in niza]
                        boxes_ = list(boxes_)
                        boxes_.remove(box)
                new_state = (new_covek, tuple(boxes_))
                successors[move] = new_state
        return successors

if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    problem = Boxes((man_pos, tuple(boxes)),n,tuple(boxes))

    res = breadth_first_graph_search(problem)

    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")