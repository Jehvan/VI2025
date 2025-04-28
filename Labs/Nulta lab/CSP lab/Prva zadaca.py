from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # Define meeting hours (only full hours between 12:00 and 20:00)
    meeting_times = list(range(12, 20))

    # Define available slots per person
    simona_available = {13, 14, 16, 19}
    marija_available = {14, 15, 18}
    petar_available = {12, 13, 16, 17, 18, 19}

    # Define variables
    problem.addVariable("vreme_sostanok", meeting_times)  # Meeting time
    problem.addVariable("Simona_prisustvo", (0, 1))  # 1 if present, 0 if not
    problem.addVariable("Marija_prisustvo", (0, 1))  # 1 if present, 0 if not
    problem.addVariable("Petar_prisustvo", (0, 1))  # 1 if present, 0 if not

    # Constraint: Simona must be present at the meeting time
    def simona_must_attend(meeting_time, simona):
        return simona == 1 if meeting_time in simona_available else simona == 0

    problem.addConstraint(simona_must_attend, ["vreme_sostanok", "Simona_prisustvo"])

    # Constraint: Marija's availability
    def marija_attendance(meeting_time, marija):
        return marija == 1 if meeting_time in marija_available else marija == 0

    problem.addConstraint(marija_attendance, ["vreme_sostanok", "Marija_prisustvo"])

    # Constraint: Petar's availability
    def petar_attendance(meeting_time, petar):
        return petar == 1 if meeting_time in petar_available else petar == 0

    problem.addConstraint(petar_attendance, ["vreme_sostanok", "Petar_prisustvo"])

    # Constraint: At least one more person must be present with Simona
    def at_least_one_more(simona, marija, petar):
        return simona == 1 and (marija == 1 or petar == 1)

    problem.addConstraint(at_least_one_more, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])

    # Print solutions
    for solution in problem.getSolutions():
        print(solution)
