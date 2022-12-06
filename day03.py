alphabet = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getInputs():
    with open("day03input.txt") as source:
        return [row.strip() for row in source]        

def findDuplicate(rucksack):
    compartment1, compartment2 = set(rucksack[0:int(len(rucksack)/2)]), set(rucksack[int(len(rucksack)/2):])
    for item in compartment1:
        if item in compartment2:
            return item

def getScore(item):
    return alphabet.index(item)

def part1():
    inputs = getInputs()
    return sum(getScore(findDuplicate(rucksack)) for rucksack in inputs)

def findTruplicate(set1, set2, set3):
    for item in set1:
        if item in set2 and item in set3:
            return item

def part2():
    inputs = getInputs()
    total = 0
    while len(inputs):
        set1 = set(inputs.pop(0))
        set2 = set(inputs.pop(0))
        set3 = set(inputs.pop(0))
        total += getScore(findTruplicate(set1, set2, set3))
    return total

print(part2())
print(part1())