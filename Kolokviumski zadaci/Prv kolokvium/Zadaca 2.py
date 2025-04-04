from constraint import *

def around(drvo):
    okolu = ((0,1),(0,-1),(1,0),(-1,0))
    lista = []
    for x,y in okolu:
        if 0 <= drvo[0] + x < 6 and 0 <= drvo[1] + y < 6 and (drvo[0] + x, drvo[1] + y) not in trees:
            lista.append((drvo[0] + x, drvo[1]+y))
    return lista

def around_shatori(*shatori):
    okolu = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1))
    for x,y in okolu:
        for shator in shatori:
            new_shator = (shator[0] + x, shator[1] + y)
            if 0 <= new_shator[0] < 6 and 0 <= new_shator[1] < 6:
                if new_shator in shatori:
                    return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    n = int(input())
    trees = ()
    for _ in range(n):
        koordinati = tuple(map(int, input().split()))
        trees += (koordinati,)
    for tree in trees:
        problem.addVariable(tree, around(tree))
    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----
    problem.addConstraint(AllDifferentConstraint(),trees)
    problem.addConstraint(around_shatori,trees)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------

    #problem.addConstraint(..., ...)

    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----
    for tree in trees:
        print(solution[tree][0], solution[tree][1])


