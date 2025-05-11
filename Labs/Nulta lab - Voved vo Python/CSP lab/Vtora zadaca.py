from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Defining the variables (papers)
    variables = list(papers.keys())

    # Defining the domain (time slots)
    domain = [f'T{i + 1}' for i in range(num)]

    # Initializing the problem
    problem = Problem(BacktrackingSolver())

    # Adding variables to the problem
    problem.addVariables(variables, domain)

    # Group papers by topic
    topics = dict()
    for paper, topic in papers.items():
        if topic not in topics:
            topics[topic] = [paper]
        else:
            topics[topic].append(paper)

    # Apply constraints: if the number of papers in a topic is <= 4, they should be assigned to the same time slot
    for topic, group in topics.items():
        if len(group) <= 4:
            problem.addConstraint(AllEqualConstraint(), group)

    # Use getSolutionIter() instead of getSolutions() to avoid memory overload
    valid_solution_found = False
    for res in problem.getSolutionIter():
        counts = {'T1': 0, 'T2': 0, 'T3': 0, 'T4': 0}
        # Count the number of papers assigned to each time slot
        for v in res.values():
            counts[v] += 1

        # Ensure no time slot has more than 4 papers
        if all(c <= 4 for c in counts.values()):
            valid_solution_found = True
            # Print the valid solution
            for paper in sorted(res.keys()):
                print(f"{paper} ({papers[paper]}): {res[paper]}")
            break  # Stop after finding the first valid solution

    if not valid_solution_found:
        print("No valid solution found.")
