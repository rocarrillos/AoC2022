def getInputs():
    with open("day04input.txt") as source:
        return [row.strip().split(',') for row in source]

def prepareAssignments(assignments):
    assignments = [i.split('-') for i in assignments]
    for assignment in assignments:
        for i in range(len(assignment)):
            assignment[i] = int(assignment[i])
    return assignments

def compare(assignments):
    assignments = prepareAssignments(assignments)    
    containment1 = assignments[0][0] <= assignments[1][0] and assignments[0][1] >= assignments[1][1]
    containment2 = assignments[1][0] <= assignments[0][0] and assignments[1][1] >= assignments[0][1]
    return 1 if containment1 or containment2 else 0

def part1():
    inputs = getInputs()
    return sum(compare(i) for i in inputs)

print(part1())

def compare2(assignments):
    assignments = prepareAssignments(assignments)
    containment1 = assignments[0][0] <= assignments[1][1] <= assignments[0][1]
    containment2 = assignments[1][0] <= assignments[0][1] <= assignments[1][1]
    return 1 if containment1 or containment2 else 0

def part2():
    inputs = getInputs()
    return sum(compare2(i) for i in inputs)

print(part2())