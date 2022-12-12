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
    
    board = []
    for i in range(20):
        col = []
        for j in range(20):
            col.append('.')
        board.append(col)

    visitedTailSpaces = [
        {'x':0, 'y':0}
    ]

    # Start at 0,0 arbitrarily
    headX = int(0)
    headY = int(0)
    tailSize = 9
    tailPieces = {}
    # Need to use headPiece, not headX/Y, cause its throwing off.
    headPiece = {
        'x': 0,
        'y': 0
    }
    # board[headY+10][headX+10] = 'h'
    for i in range(tailSize):
        tailPieces[i] = {
            'x': 0,
            'y': 0
        }

    # This gets each line.
    for direction, amountOfSteps in directionParts:
        # This loops over the step amount.
        for step in range(int(amountOfSteps)):
            # board[headY+10][headX+10] = '.'
            headX = headPiece['x']
            headY = headPiece['y']

            # previousHeadX = int(headX)
            # previousHeadY = int(headY)
            # Head only ever moves 1.
            if direction == 'R':
                headX += 1
            elif direction == 'L':
                headX -= 1
            elif direction == 'U':
                headY -= 1
            elif direction == 'D':
                headY += 1
            headPiece['x'] = headX  
            headPiece['y'] = headY
            print()
            print(f"Head is moving. Current X: {headX}, Current Y: {headY}")
            
            for tail, tailCoords in tailPieces.items():
                # The tail is always going to be the next piece.
                tailX = tailCoords['x']
                tailY = tailCoords['y']
                # If the index is the first part of the tail,
                # We want to follow the head. Else we want to follow the 
                # h-1 tail piece.
                if tail != 0:
                    headX = tailPieces[tail-1]['x']
                    headY = tailPieces[tail-1]['y']
                    print(f"Tail {tail} is not the first tail, so follow tail {tail-1}.")
                    print(f"New \"Head\" X: {headX}, Y: {headY}")
                else:
                    headX = headPiece['x']
                    headY = headPiece['y']
                # Head has moved adjacent but to a corner.
                if headX != tailX and headY != tailY:
                    if (
                        headX >= tailX + 2 or
                        headX <= tailX - 2 or
                        headY >= tailY + 2 or
                        headY <= tailY - 2
                    ):
                        print("DIAGONAL. diraction: ", direction)
                        print("TailX", tailX, "TailY", tailY)
                        print("HeadX", headX, "HeadY", headY)
                        # HeadY < means it is taller/higher
                        if headY < tailY:
                            tailY -= 1
                            if headX > tailX:
                                tailX += 1
                            if headX < tailX:
                                tailX -= 1
                        if headY > tailY:
                            tailY += 1
                            if headX > tailX:
                                tailX += 1
                            if headX < tailX:
                                tailX -= 1

                        # for i in range(2):
                        #     # Need to move up and over.
                        #     # if direction == 'U':
                        #     print(f"IF {tailY} > {headY+1}")
                        #     if headY +1 <= tailY:
                        #     # if tailY > headY+1:
                        #         # print("Move up")
                        #         tailY -= 1
                        #     else:
                        #         # print("Move over")
                        #         # Move tail right 1
                        #         if headX > tailX:
                        #             motion = 'UR'
                        #             tailX += 1
                        #         # Move tail left 1
                        #         else:
                        #             motion = 'UL'
                        #             tailX -= 1
                        # # elif direction == 'D':
                        #     if tailY < headY-1:
                        #         tailY += 1
                        #     else:
                        #         if headX > tailX:
                        #             motion = 'DR'
                        #             tailX += 1
                        #         else:
                        #             motion = 'DL'
                        #             tailX -= 1
                        # # elif direction == 'R':
                        #     if tailX < headX-1:
                        #         tailX += 1
                        #     else:
                        #         if tailY > headY:
                        #             motion = 'UR'
                        #             tailY -= 1
                        #         else:
                        #             motion = 'DR'
                        #             tailY += 1
                        # # elif direction == 'L':
                        #     # print("Move left 1, up/down 1")
                        #     if tailX > headX + 1:
                        #         tailX -= 1
                        #     else:
                        #         if tailY > headY:
                        #             motion = 'UL'
                        #             tailY -= 1
                        #         else:
                        #             motion = 'DL'
                        #             tailY += 1
                        # Update dict.
                        tailPieces[tail]['x'] = tailX
                        tailPieces[tail]['y'] = tailY
                else:    
                    # print("TAA", tailX, tailY)
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
                tailPieces[tail]['x'] = tailX
                tailPieces[tail]['y'] = tailY                   
                print(f"Tail {tail} moved. Current X: {tailX}, Current Y: {tailY}")
                if (tail == 8):
                    visitedTailSpaces.append({'x': tailPieces[tail]['x'], 'y': tailPieces[tail]['y']})
                # print("Head location: ", headX, headY)
                # print("Tail location: ", tailPieces[tail]['x'], tailPieces[tail]['y'])
                # if tail == len(tailPieces)-1:

                # board[headY+10][headX+10] = 'h'
                # board[tailY+10][tailX+10] = f'{tail}'
            # for row in board:
            #     print(row)

    uniqueTailSteps = []
    for visitedSpace in visitedTailSpaces:
        if visitedSpace not in uniqueTailSteps:
            uniqueTailSteps.append(visitedSpace)
    print(uniqueTailSteps)
    print("Visited tail spaces", len(visitedTailSpaces))
    print("Unique tail spaces", len(uniqueTailSteps))


                
            # if tailX != headX and tailY != headY:
            #     if (
            #         headX >= tailX + 2 or    
            #         headX <= tailX - 2 or
            #         headY >= tailY + 2 or
            #         headY <= tailY - 2 
            #     ):
            #         print("Need to move diagonally!")
            #         for i in range(2):
            #             # If the direction was up, 
            #             # need to move up by -1, 
            #             # and set the column to 
            #             # hY-1
            #             if direction == 'U':
            #                 # The direction is up. If
            #                 # We are not on the same adjacent X level
            #                 # We need to increase so we are.
            #                 if tailX < headX:
            #                     tailX += 1
            #                 # If we are on the same level,
            #                 # Now we just need to move one closer.
            #                 # If the head is on the right, the Y will be higher
            #                 # If the head is on the left, the Y will be lower
            #                 else:
            #                     if headY < tailY:
            #                         tailY += 1
            #                     else:
            #                         tailY -= 1
            #             elif direction == 'D':
            #                 if tailX > headX:
            #                     tailX -= 1
            #                 else:
            #                     if headY < tailY:
            #                         tailY += 1
            #                     else:
            #                         tailY -= 1
            #             # If the direction is to the right the head is no
            #             # longer adjacent 
            #             # We need to move to the right once so we are in adjacent
            #             # level
            #             elif direction == 'R':
            #                 # Now we move the tail to the right, and its now
            #                 # in the same adjacent level.
            #                 if tailY < headY:
            #                     tailY += 1
            #                 # Now we need to move closer to the X level.
            #                 else:
            #                     if tailX < headX:
            #                         tailX -= 1
            #                     else:
            #                         tailX += 1
            #             elif direction == 'L':
            #                 if tailY > headY:
            #                     tailY -= 1
            #                 else:
            #                     if tailX > headX:
            #                         tailX += 1
            #                     else:
            #                         tailX -=

                        # elif direction == 'R':
                        # elif direction == 'L':
                        # elif direction == 'D':
                    # tailX = previousHeadX
                    # tailY = previousHeadY
            # else:    
            #     # Now that the head has moved, need to determine if the tail should move.
            #     # The tail should move if it is not adjacent to the head.
            #     if headX >= tailX + 2:
            #         tailX += 1
            #     elif headX <= tailX - 2:
            #         tailX -= 1
            #     elif headY >= tailY + 2:
            #         tailY += 1
            #     elif headY <= tailY - 2:
            #         tailY -= 1

# Need to define a diagonal step, and only track 1 for it
# It doesn't matter how the step gets executed,
# so long as the final position only counts as 1 movement.
# We 'teleported' because we didn't want to track a step.

# .....    .....    .....
# .....    ..H..    ..H..
# ..H.. -> ..... -> ..T..
# .T...    .T...    .....
# .....    .....    .....

# Need to move from teleporting to moving diagonally
# and tracking 1 step.

# == U4 ==
# ......
# ......
# ......
# ....H.
# 4321.. // Head move up one more
# ->
# ......
# ......
# ....H.
# ......
# 4321..  // H isn't touching 1. Move 1 'diagonally'
# ->
# ......
# ......
# ....H.
# ...1..
# 432...
# ->
# ......
# ......
# ....H.
# ....1.
# 432... // 1 is still moving 'diagonally'
# ->
# ......
# ......
# ....H.
# ..2.1.
# 43.... // 1 isn't touching 2. Move 2 'diagonally'
# ->
# ......
# ......
# ....H.
# ...21.
# 43.... // 2 is still moving 'diagonally'

# ......
# ......
# ....H.
# ....1.
# 432...   // 2 isn't touching 1. Set 2 to old 1. No longer works
    #         if tailX != headX and tailY != headY:
    #             if (
    #                 headX >= tailX + 2 or    
    #                 headX <= tailX - 2 or
    #                 headY >= tailY + 2 or
    #                 headY <= tailY - 2 
    #             ):
    #                 print("Not in the same row or column and 2 far away... Teleporting!")
    #                 tailX = previousHeadX
    #                 tailY = previousHeadY
    #         else:    
    #             # Now that the head has moved, need to determine if the tail should move.
    #             # The tail should move if it is not adjacent to the head.
    #             if headX >= tailX + 2:
    #                 tailX += 1
    #             elif headX <= tailX - 2:
    #                 tailX -= 1
    #             elif headY >= tailY + 2:
    #                 tailY += 1
    #             elif headY <= tailY - 2:
    #                 tailY -= 1
    #         print("Head location: ", headX, headY)
    #         print("Tail location: ", tailX, tailY)
    #         # Once we move, update the visited spaces.
    #         visitedHeadSpaces.append({'x': headX, 'y': headY})
    #         visitedTailSpaces.append({'x': tailX, 'y': tailY})
    #         print()

    # uniqueHeadSteps = []
    # for visitedSpace in visitedHeadSpaces:
    #     if visitedSpace not in uniqueHeadSteps:
    #         uniqueHeadSteps.append(visitedSpace)
    # print("Visited head spaces", len(visitedHeadSpaces))
    # print("Unique head spaces", len(uniqueHeadSteps))

    # uniqueTailSteps = []
    # for visitedSpace in visitedTailSpaces:
    #     if visitedSpace not in uniqueTailSteps:
    #         uniqueTailSteps.append(visitedSpace)
    # print("Visited tail spaces", len(visitedTailSpaces))
    # print("Unique tail spaces", len(uniqueTailSteps))
        
    # assert uniqueTailSteps == 6284
 
        
if __name__ == "__main__":
    main()