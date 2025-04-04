from constraint import *

def crypt(s,e,n,d,m,o,r,y):
    send = s*1000 + e*100 + n*10 + d
    more = m*1000 + o*100 + r*10 + e
    money = m*10000 + o*1000 + n*100 + e*10 + y
    return send + more == money


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(crypt,variables)
    # ----------------------------------------------------

    print(problem.getSolution())