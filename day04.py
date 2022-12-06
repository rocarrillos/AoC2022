def getInputs():
    with open("day04input.txt") as source:
        return [prepareAssignments(i) for i in [row.strip().split(',') for row in source]]

def prepareAssignments(assignments):
    assignments = [i.split('-') for i in assignments]
    for assignment in assignments:
        for i in range(len(assignment)):
            assignment[i] = int(assignment[i])
    return assignments

def compare(assignments):
    # in the shape of [[a, b], [x, y]]
    containment1 = assignments[0][0] <= assignments[1][0] and assignments[0][1] >= assignments[1][1]
    containment2 = assignments[1][0] <= assignments[0][0] and assignments[1][1] >= assignments[0][1]
    return 1 if containment1 or containment2 else 0

def part1():
    return sum(compare(i) for i in getInputs())

def compare2(assignments):
    # in the shape of [[a, b], [x, y]]
    containment1 = assignments[0][0] <= assignments[1][1] <= assignments[0][1]
    containment2 = assignments[1][0] <= assignments[0][1] <= assignments[1][1]
    return 1 if containment1 or containment2 else 0

def part2():
    return sum(compare2(i) for i in getInputs())

print(part1())

print(part2())