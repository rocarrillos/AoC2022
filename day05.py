alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getInputs():
    inputsList = []
    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8:[], 9: []}
    instructions = []    
    with open("day05input.txt") as source:
        inputsList = [row.strip() for row in source]
    for i in range(9):
        for j in range(len(inputsList[i])):
            if inputsList[i][j] in alphabet:
                stacks[(j + 3) / 4].insert(0, (inputsList[i][j]))
    for i in range(10, len(inputsList)):
        instruction = inputsList[i].split(' ')
        instruction[1] = int(instruction[1])
        instruction[3] = int(instruction[3])
        instruction[5] = int(instruction[5])
        instructions.append(instruction)
    return stacks, instructions

def part1():
    stacks, instructions = getInputs()
    for instruction in instructions:
        amountToMove = instruction[1]
        source = instruction[3]
        destination = instruction[5]
        for i in range(amountToMove):
            crate = stacks[source].pop()
            stacks[destination].append(crate)
    return stacks

print(part1())

def part2():
    stacks, instructions = getInputs()
    for instruction in instructions:
        amountToMove = instruction[1]
        source = instruction[3]
        destination = instruction[5]
        crates = []
        for i in range(amountToMove):
            crates.insert(0, stacks[source].pop())
        stacks[destination].extend(crates)
    return stacks

print(' ')
print(part2())