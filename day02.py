rock = 'rock'
paper = 'paper'
scissors = 'scissors'

playScoresDict = {rock: 1, paper: 2, scissors: 3}
part1map = {'X': rock, 'Y': paper, 'Z': scissors}
winScore = 6
tieScore = 3
lossScore = 0

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
        return winScore
    elif (play[0] == 'A' and play[1] == 'X') or (play[0] == 'B' and play[1] == 'Y') or (play[0] == 'C' and play[1] == 'Z'):
        # tie conditions
        return tieScore
    else:
        return lossScore

def getPlayScore(play):
    # in the shape of [A, X]
    return playScoresDict.get(part1map.get(play[1]))

def part1():
    inputs = getInputs()
    print(inputs[0])
    matchScores = sum(map(lambda i: getMatchScore(i), inputs))
    playScores = sum(map(lambda i: getPlayScore(i), inputs))
    return matchScores + playScores

print(part1())

# part 2 below

def getMatchScore2(play):
    # in the shape of [A, X]
    outcome = play[1]
    match outcome:
        case 'Z': return getWinningMove(play[0]) + winScore
        case 'Y': return getTyingMove(play[0]) + tieScore
        case 'X': return getLosingMove(play[0]) + lossScore

def getWinningMove(opponentMove):
    match opponentMove:
        case 'A': return 2
        case 'B': return 3
        case 'C': return 1

def getTyingMove(opponentMove):
    match opponentMove:
        case 'A': return 1
        case 'B': return 2
        case 'C': return 3

def getLosingMove(opponentMove):
    match opponentMove:
        case 'A': return 3
        case 'B': return 1
        case 'C': return 2

def part2():
    return sum(getMatchScore2(play) for play in getInputs())

print(part2())
