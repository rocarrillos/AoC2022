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

print(part1())