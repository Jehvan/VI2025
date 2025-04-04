from constraint import *



if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    simona_time = (13,14,16,19)
    petar_time = (12,13,16,17,18,19)
    marija_time = (14,15,18)
    times = range(12,20)

    def simona_available(time,prisustvo):
        if time in simona_time:
            return True
        return prisustvo == 0

    def marija_available(time,prisustvo):
        if time in marija_time:
            return True
        return prisustvo == 0


    def petar_available(time,prisustvo):
        if time in petar_time:
            return True
        return prisustvo == 0

    def barem_dva(simona,marija, petar):
        return 1 if marija + simona > 1 or petar + simona > 1 else 0
    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", (0, 1))
    problem.addVariable("Marija_prisustvo", (0,1))
    problem.addVariable("Petar_prisustvo", (0,1))
    problem.addVariable("vreme_sostanok", range(12,20))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(barem_dva, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])
    problem.addConstraint(simona_available, ["vreme_sostanok","Simona_prisustvo"])
    problem.addConstraint(petar_available, ["vreme_sostanok","Petar_prisustvo"])
    problem.addConstraint(marija_available, ["vreme_sostanok","Marija_prisustvo"])
     # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]