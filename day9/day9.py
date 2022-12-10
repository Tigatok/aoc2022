def main():
    inputFile = open("./input_e.txt", "r")
    inputFile = inputFile.read()
    solution(inputFile)

# Get direction parts.
def getDirectionParts(inputFile):
    directionParts = []
    for directionLine in inputFile:
        directionPart = directionLine.split(' ')
        directionParts.append([directionPart[0],directionPart[1]])
    return directionParts

def solution(inputFile):
    directionLines = inputFile.split('\n')
    directionParts = getDirectionParts(directionLines)
    
    visitedSpaces = []

    # Start at 0,0 arbitrarily
    headX = int(0)
    headY = int(0)
    for direction, amountOfSteps in directionParts:
        for step in range(int(amountOfSteps)):
            currX = int(headX)
            currY = int(headY)
            visitedSpaces.append({'x': currX, 'y': currY})

            if direction == 'R':
                headX += 1
            elif direction == 'L':
                headX -= 1
            elif direction == 'U':
                headY -= 1
            elif direction == 'D':
                headY += 1
            print("Old location: ", currX, currY)
            print("New location: ", headX, headY)
            print()

    uniqueSteps = []
    for visitedSpace in visitedSpaces:
        if visitedSpace not in uniqueSteps:
            uniqueSteps.append(visitedSpace)
        else:
            print(visitedSpace, " has already been visited")
    print("Visited spaces", len(visitedSpaces))
    print("Unique spaces", len(uniqueSteps))
        
    assert headX == 2
    assert headY == -2
    assert len(uniqueSteps) == 21
 
        
if __name__ == "__main__":
    main()