def getCaloriesPerElf():
    elves = []
    
    with open('day01input.txt') as source:
        tempArray = []
        for row in source:
            if len(row) > 1:
                tempArray.append(int(row.strip()))
            else:
                elves.append(tempArray)
                tempArray = []
    
    return map(lambda i: sum(i), elves)
    
def part1():
    return max(getCaloriesPerElf())

def part2():
    return sum(sorted(getCaloriesPerElf())[-3:])


print(part1(), part2())