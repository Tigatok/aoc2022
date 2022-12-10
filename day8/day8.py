def main():
    day8 = open("./day8.txt", "r")
    day8 = day8.read()
    solutionOne(day8)

# 529 is too low
def solutionOne(input):
    mapRow = input.split('\n')
    print(mapRow)
    coordinates = []
    for row in mapRow:
        rows = list(row)
        coordinates.append(rows)

    print("Coordinates\n")
    for row in coordinates:
        print(row)
    
    # it's a perfect square.
    mapSize = len(coordinates)
    print("Map Size:", mapSize)

    treesToSearch = []
    internalVisibleTrees = 0
    for x in range(mapSize):
        for y in range(mapSize):
            tree = int(coordinates[x][y])
            treesToSearch.append(tree)
            print("Searching with tree", tree)
            downTrees = []
            rightTrees = []
            upTrees = []
            leftTrees = []
            # Initialize to 1 so we don't count the tree we are looking around.
            count = 1
            # We know the tree we are looking at.
            # Now, we need to get all other trees around that one.
            while count < mapSize:
                xCount = int(x) + count
                yCount = int(y) + count
                nXCount = int(x) - count
                nYCount = int(y) - count
                if (xCount) < len(coordinates[x]):
                    # Increment right away or else we will be on the same tree...
                    checkTree = int(coordinates[xCount][y])
                    downTrees.append(checkTree)
                if (yCount) < len(coordinates[y]):
                    checkTree = int(coordinates[x][yCount])
                    rightTrees.append(checkTree)
                if (nXCount >= 0):
                    checkTree = int(coordinates[nXCount][y])
                    upTrees.append(checkTree)
                if (nYCount >= 0):
                    checkTree = int(coordinates[x][nYCount])
                    leftTrees.append(checkTree)
                count += 1
            print("Up", upTrees)
            print("Right", rightTrees)
            print("Down", downTrees)
            print("Left", leftTrees)

            visibleFromUp = False
            if len(upTrees) == 0:
                visibleFromUp = True
            else:
                for upTree in upTrees:
                    print(tree, ">", upTree, tree>upTree)
                    if tree > upTree:
                        visibleFromUp = True
                    else:
                        visibleFromUp = False
                        break
            # true

            visibleFromRight = False
            if len(rightTrees) == 0:
                visibleFromRight = True
            else:
                for rightTree in rightTrees:
                    print(tree, ">", rightTree, tree>rightTree)
                    if tree > rightTree:
                        visibleFromRight = True
                    else:
                        visibleFromRight = False
                        break

            visibleFromDown = False
            if len(downTrees) == 0:
                visibleFromDown = True
            else:
                for downTree in downTrees:
                    print(tree, ">", downTree, tree>downTree)
                    if tree > downTree:
                        visibleFromDown = True
                    else:
                        visibleFromDown = False
                        break

            visibleFromLeft = False
            if len(leftTrees) == 0:
                visibleFromLeft = True
            else:
                for leftTree in leftTrees:
                    print(tree, ">", leftTree, tree>leftTree)
                    if tree > leftTree:
                        visibleFromLeft = True
                    else:
                        visibleFromLeft = False
                        break;
            treeIsVisible = False
            if (visibleFromUp or visibleFromDown or visibleFromLeft or visibleFromRight):
                treeIsVisible = True
            if treeIsVisible == True:
                internalVisibleTrees += 1

            print("Tree", tree,"is visible:", treeIsVisible)
            print()
    totalVisibleTrees =  internalVisibleTrees
    print(totalVisibleTrees)

if __name__ == "__main__":
    main()