
def getInputs():
    inputs = []
    with open("day02input.txt") as source:
        for row in source:
            row = row.strip().replace(" ", "")
            inputs.append([row[0], row[1]])
    return inputs

def getMatchScore(play):
    # in the shape of [A, X]
    if (play[0] == 'A' and play[1] == 'Y') or (play[0] == 'B' and play[1] == 'Z') or (play[0] == 'C' and play[1] == 'X'):
        # win conditions
        return 6
    elif (play[0] == 'A' and play[1] == 'X') or (play[0] == 'B' and play[1] == 'Y') or (play[0] == 'C' and play[1] == 'Z'):
        # tie conditions
        return 3
    else:
        return 0

def getPlayScore(play):
    # in the shape of [A, X]
    if play[1] == 'X':
        return 1
    elif play[1] == 'Y':
        return 2
    else:
        return 3

def part1():
    inputs = getInputs()
    print(inputs[0])
    matchScores = sum(map(lambda i: getMatchScore(i), inputs))
    playScores = sum(map(lambda i: getPlayScore(i), inputs))
    return matchScores + playScores

print(part1())

# part 2 below
