def main():
    day8 = open("./day8_2.txt", "r")
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
    print("Perimiter Trees:", getPerimiterTrees(mapSize))

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
            treeIsVisible = False
            if len(upTrees) == 0:
                treeIsVisible = True
            else:
                for upTree in upTrees:
                    print(tree, ">", upTree, tree>upTree)
                    if tree > upTree:
                        treeIsVisible = True
                    else:
                        break
            # true

            if len(rightTrees) == 0:
                treeIsVisible = True
            else:
                for rightTree in rightTrees:
                    print(tree, ">", rightTree, tree>rightTree)
                    if tree > rightTree:
                        treeIsVisible = True
                    else:
                        break

            if len(downTrees) == 0:
                treeIsVisible = True
            else:
                for downTree in downTrees:
                    print(tree, ">", downTree, tree>downTree)
                    if tree > downTree:
                        treeIsVisible = True
                    else:
                        break

            if len(leftTrees) == 0:
                treeIsVisible = True
            else:
                for leftTree in leftTrees:
                    print(tree, ">", leftTree, tree>leftTree)
                    if tree > leftTree:
                        treeIsVisible = True
                    else:
                        break
            if treeIsVisible == True:
                internalVisibleTrees += 1
            print("Tree", tree,"is visible:", treeIsVisible)
            print()
               
            # treeIsVisible = False
            # for neighborTree in upTrees:
            #     if tree > neighborTree:
            #         treeIsVisible = True
            #     else:
            #         break
            # for neighborTree in rightTrees:
            #     if tree > neighborTree:
            #         treeIsVisible = True
            #     else:
            #         break
            # for neighborTree in downTrees:
            #     if tree > neighborTree:
            #         treeIsVisible = True
            #     else:
            #         break
            # for neighborTree in leftTrees:
            #     if tree > neighborTree:
            #         treeIsVisible = True
            #     else:
            #         break
            # if treeIsVisible:
            #     print("Tree",tree,"is visible\n")
            #     internalVisibleTrees += 1
            # else:
            #     print()
    totalVisibleTrees =  internalVisibleTrees
    print(totalVisibleTrees)
    assert totalVisibleTrees == 31


# def isVisible(tree, coordinates):
#     # I have the tree that I am searching for.
#     return False

# This should probably actually return the trees
# that make up the permiter.. Some dict.
def getPerimiterTrees(mapSize):
    perimiterTrees = 0

    # Loop over all the rows
    for x in range(mapSize):
        # Loop over all the columns
        for y in range(mapSize):
            if (
                x == 0 or
                y == 0 or
                y == mapSize-1 or
                x == mapSize-1
            ):
                perimiterTrees += 1
    return int(perimiterTrees)

if __name__ == "__main__":
    main()