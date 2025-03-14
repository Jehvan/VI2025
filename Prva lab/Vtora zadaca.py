from searching_framework import Problem, \
    breadth_first_graph_search
# define your Problem class here


def bounds(tmp):
    if 0 <= tmp[0] < 8 and 0 <= tmp[1] < 6:
        return True
    return False

def check_state(state,protivnici):
    okolina_protivnici = (
        (protivnici[0][0] - 1, protivnici[0][1] + 1), (protivnici[0][0], protivnici[0][1] + 1),
        (protivnici[0][0] + 1, protivnici[0][1] + 1),
        (protivnici[0][0] - 1, protivnici[0][1]), (protivnici[0][0], protivnici[0][1]),
        (protivnici[0][0] + 1, protivnici[0][1]),
        (protivnici[0][0] - 1, protivnici[0][1] - 1), (protivnici[0][0] - 1, protivnici[0][1]),
        (protivnici[0][0] + 1, protivnici[0][1] - 1),
        (protivnici[1][0] - 1, protivnici[1][1] + 1), (protivnici[1][0], protivnici[1][1] + 1),
        (protivnici[1][0] + 1, protivnici[1][1] + 1),
        (protivnici[1][0] - 1, protivnici[1][1]), (protivnici[1][0], protivnici[1][1]),
        (protivnici[1][0] + 1, protivnici[1][1]),
        (protivnici[1][0] - 1, protivnici[1][1] - 1), (protivnici[1][0] - 1, protivnici[1][1]),
        (protivnici[1][0] + 1, protivnici[1][1] - 1),
    )
    if state[0] in protivnici:
        return False
    if state[1] in okolina_protivnici:
        return False
    if bounds(state[0]) and bounds(state[1]):
        return True
    else:
        return False

class Fudbaler(Problem):
    def __init__(self, initial_state,protivnici,gol,goal=None):
        super().__init__(initial_state, goal=None)
        self.protivnici = protivnici
        self.gol = gol


    def successor(self, state):
        successors = dict()
        movements = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        covek_movements = (
            "Pomesti coveche gore", "Pomesti coveche gore-desno", "Pomesti coveche desno", "Pomesti coveche dolu-desno",
            "Pomesti coveche dolu")
        so_topce_movements = (
            "Turni topka gore", "Turni topka gore-desno", "Turni topka desno", "Turni topka dolu-desno",
            "Turni topka dolu")
        covek = state[0]
        topce = state[1]
        for move, topce_move, covek_move  in zip(movements,so_topce_movements,covek_movements):
            new_covek = (covek[0] + move[0], covek[1] + move[1])
            if new_covek == topce:
                new_topce = (new_covek[0]+ move[0], new_covek[1]+ move[1])
                new_state = (new_covek, new_topce)
                if check_state(new_state,self.protivnici):
                    new_state = (tuple(new_covek), tuple(new_topce))
                    successors[topce_move] = new_state
            else:
                new_state = (new_covek, topce)
                if check_state(new_state,self.protivnici):
                    new_state = (tuple(new_covek), tuple(topce))
                    successors[covek_move] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state[1] in self.gol




if __name__ == '__main__':
    vlez1 = input().split(",")
    vlez2 = input().split(",")
    covece = (int(vlez1[0]), int(vlez1[1]))
    topka = (int(vlez2[0]), int(vlez2[1]))
    protivnici = ((3, 3), (5, 4))
    gol = ((7, 2), (7, 3))
    fudbaler = Fudbaler((tuple(covece), tuple(topka)),protivnici,gol)
    result = breadth_first_graph_search(fudbaler)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")