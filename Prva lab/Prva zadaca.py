from searching_framework import Problem, \
    breadth_first_graph_search  # , just an example, import whatever you actually need from the searching framework

# note that your program won't work if you copy and paste classes instead of import them via the above statement

# define your Problem class here
pravo = ((0, 1), (1, 0), (0, -1), (-1, 0))
levo = ((-1, 0), (0, 1), (1, 0), (0, -1))
desno = ((1, 0), (0, -1), (-1, 0), (0, 1))
nasoki = (pravo, levo, desno)


def is_valid(head, body, red_apples):
    a = head[0]
    b = head[1]
    shirina, visina = 10, 10
    if not (0 <= a < shirina and 0 <= b < visina):
        return False
    if head in body or head in red_apples:
        return False
    return True


def straight(body, nasoka, red_apples):
    head = body[-1]
    newx = head[0] + pravo[nasoka][0]
    newy = head[1] + pravo[nasoka][1]
    newhead = (newx, newy)
    if is_valid(newhead, body, red_apples):
        return newhead
    else:
        return head


def left(body, nasoka, red_apples):
    head = body[-1]
    newx = head[0] + levo[nasoka][0]
    newy = head[1] + levo[nasoka][1]
    newhead = (newx, newy)
    if is_valid(newhead, body, red_apples):
        return newhead
    else:
        return head


def right(body, nasoka, red_apples):
    head = body[-1]
    newx = head[0] + desno[nasoka][0]
    newy = head[1] + desno[nasoka][1]
    newhead = (newx, newy)
    if is_valid(newhead, body, red_apples):
        return newhead
    else:
        return head


class Snake(Problem):
    def __init__(self, red_apples, initial_state, goal_state=None):
        super().__init__(initial_state, goal_state)
        self.red_apples = red_apples

    def successor(self, state):
        successors = dict()
        body = list(state[0])
        head = body[-1]
        nasoka = state[1]
        green_apples = list(state[2])

        pravosnake = body[:]
        pravogreen = green_apples[:]
        new_head = straight(body, nasoka, self.red_apples)
        if new_head != head:
            pravosnake.append(new_head)
            if new_head not in green_apples:
                pravosnake.pop(0)
            else:
                pravogreen.remove(new_head)
            successors["ProdolzhiPravo"] = tuple(pravosnake), nasoka, tuple(pravogreen)

        levosnake = body[:]
        levogreen = green_apples[:]
        new_head = left(body, nasoka, self.red_apples)
        if new_head != head:
            levosnake.append(new_head)
            if new_head not in green_apples:
                levosnake.pop(0)
            else:
                levogreen.remove(new_head)
            successors["SvrtiLevo"] = tuple(levosnake), (nasoka - 1) % 4, tuple(levogreen)

        desnosnake = body[:]
        desnogreen = green_apples[:]
        new_head = right(body, nasoka, self.red_apples)
        if new_head != head:
            desnosnake.append(new_head)
            if new_head not in green_apples:
                desnosnake.pop(0)
            else:
                desnogreen.remove(new_head)
            successors["SvrtiDesno"] = tuple(desnosnake), (nasoka + 1) % 4, tuple(desnogreen)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':
    zeleni = list()
    crveni = list()
    n = int(input())
    for i in range(n):
        x, y = input().split(",")
        x = int(x)
        y = int(y)
        zeleni.append((x, y))

    m = int(input())
    for i in range(m):
        x, y = input().split(",")
        x = int(x)
        y = int(y)
        crveni.append((x, y))
    zmija = list()
    zmija.append((0, 9))
    zmija.append((0, 8))
    zmija.append((0, 7))
    snake = Snake(tuple(crveni), (tuple(zmija), 2, tuple(zeleni)))
    result = breadth_first_graph_search(snake)
    if result is not None:
        print(result.solution())
    else:
        print("[]")
