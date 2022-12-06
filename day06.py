startOfPacketMarker = 4
startOfMessageMarker = 14

def getInputs():
    with open('day06input.txt') as source:
        return [row.strip() for row in source][0]

def getIndex(markerLength):
    input = getInputs()
    for i in range(len(input) - markerLength):
        subset = input[i:i + markerLength]
        if len(set(subset)) == markerLength:
            return i + markerLength

print(getIndex(startOfPacketMarker))
print(getIndex(startOfMessageMarker))