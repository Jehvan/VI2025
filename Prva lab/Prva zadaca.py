from searching_framework import Problem, breadth_first_graph_search #, just an example, import whatever you actually need from the searching framework
# note that your program won't work if you copy paste classes instead of import them via the above statement

# define your Problem class here

class Snake(Problem):
    def __init__(self, green_apples,red_apples,start, goal):
        super().__init__(start, goal)
        self.green_apples = green_apples
        self.red_apples = red_apples

    def successor(self, state):
        successors = dict()


        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return self.green_apples == 0
if __name__ == '__main__':
    zeleni = []
    n = int(input())
    for i in range (n):
        x,y = input().split(",")
        x = int(x)
        y = int(y)
        zeleni.append([x,y])
    crveni = []
    m = int(input())
    for i in range(m):
        x,y = input().split(",")
        x = int(x)
        y = int(y)
        crveni.append([x,y])

