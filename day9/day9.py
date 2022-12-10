def main():
    inputFile = open("./input.txt", "r")
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
    
    visitedHeadSpaces = [
        {'x':0, 'y':0}
    ]
    visitedTailSpaces = [
        {'x':0, 'y':0}
    ]

    # Start at 0,0 arbitrarily
    headX = int(0)
    headY = int(0)
    tailX = int(0)
    tailY = int(0)
    # This gets each line.
    for direction, amountOfSteps in directionParts:
        # This loops over the step amount.
        for step in range(int(amountOfSteps)):
            # May not care about old location...
            previousHeadX = int(headX)
            previousHeadY = int(headY)
            
            # Move the head first.
            if direction == 'R':
                headX += 1
            elif direction == 'L':
                headX -= 1
            elif direction == 'U':
                headY -= 1
            elif direction == 'D':
                headY += 1

            # IF the tail is not UDLR
            # AND the head is 2 spaces away
            # The tail must become the old head
            # If the tail is not in the same row or column
            # Then it is not udlr
            # We don't need to teleport if they are exactly 
            # adjacent.
            # We can't teleport to the new head location
            # We need to teleport to the old head location...
            if tailX != headX and tailY != headY:
                if (
                    headX >= tailX + 2 or    
                    headX <= tailX - 2 or
                    headY >= tailY + 2 or
                    headY <= tailY - 2 
                ):
                    print("Not in the same row or column and 2 far away... Teleporting!")
                    tailX = previousHeadX
                    tailY = previousHeadY
            else:    
                # Now that the head has moved, need to determine if the tail should move.
                # The tail should move if it is not adjacent to the head.
                if headX >= tailX + 2:
                    tailX += 1
                elif headX <= tailX - 2:
                    tailX -= 1
                elif headY >= tailY + 2:
                    tailY += 1
                elif headY <= tailY - 2:
                    tailY -= 1
            print("Head location: ", headX, headY)
            print("Tail location: ", tailX, tailY)
            # Once we move, update the visited spaces.
            visitedHeadSpaces.append({'x': headX, 'y': headY})
            visitedTailSpaces.append({'x': tailX, 'y': tailY})
            print()

    uniqueHeadSteps = []
    for visitedSpace in visitedHeadSpaces:
        if visitedSpace not in uniqueHeadSteps:
            uniqueHeadSteps.append(visitedSpace)
    print("Visited head spaces", len(visitedHeadSpaces))
    print("Unique head spaces", len(uniqueHeadSteps))

    uniqueTailSteps = []
    for visitedSpace in visitedTailSpaces:
        if visitedSpace not in uniqueTailSteps:
            uniqueTailSteps.append(visitedSpace)
    print("Visited tail spaces", len(visitedTailSpaces))
    print("Unique tail spaces", len(uniqueTailSteps))
        
    # assert headX == 2
    # assert headY == -2
    # assert tailY == -2
    # assert tailX == 1
    # assert len(uniqueHeadSteps) == 21
 
        
if __name__ == "__main__":
    main()