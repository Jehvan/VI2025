from constraint import *


if __name__ == '__main__':
    problem = Problem()
    domain = range(0,8)

    rooks = range(0,8)

    problem.addVariables(rooks, domain)

    problem.addConstraint(AllDifferentConstraint())
    print(problem.getSolution())