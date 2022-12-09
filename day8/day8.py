def main():
    day8 = open("./day8_2.txt", "r")
    day8 = day8.read()
    solutionOne(day8)

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
            # We already have the perimiter amount.
            if (
                x != 0 and
                y != 0 and
                y != mapSize-1 and
                x != mapSize-1
            ):
                tree = int(coordinates[x][y])
                treesToSearch.append(tree)
                print("Searching with tree", tree)
                count = 0
                negCount = 0
                treeIsVisible = False
                downTrees = []
                rightTrees = []
                upTrees = []
                leftTrees = []
                while count <= mapSize:
                    count+=1
                    negCount -= 1
                    xIndex = x+count
                    yIndex = y+count
                    # negXIndex = x+negCount
                    # negYIndex = y+negCount
                    if xIndex < len(coordinates[x]):
                        checkTree = int(coordinates[x+count][y])
                        downTrees.append(checkTree)
                    if yIndex < len(coordinates[y]):
                        checkTree = int(coordinates[x][y+count])
                        rightTrees.append(checkTree)

                    # Up
                    if(x-count >= 0):
                        checkTree = int(coordinates[x-count][y])
                        upTrees.append(checkTree)
                    if(y-count >= 0):
                        checkTree = int(coordinates[x][y-count])
                        leftTrees.append(checkTree)
                print("Up", upTrees)
                print("Right", rightTrees)
                print("Down", downTrees)
                print("Left", leftTrees)
                treeIsVisible = False
                for neighborTree in upTrees:
                    if tree > neighborTree:
                        treeIsVisible = True
                    else:
                        break
                for neighborTree in rightTrees:
                    if tree > neighborTree:
                        treeIsVisible = True
                    else:
                        break
                for neighborTree in downTrees:
                    if tree > neighborTree:
                        treeIsVisible = True
                    else:
                        break
                for neighborTree in leftTrees:
                    if tree > neighborTree:
                        treeIsVisible = True
                    else:
                        break
                if treeIsVisible:
                    print("Tree",tree,"is visible\n")
                    internalVisibleTrees += 1
                else:
                    print()
    totalVisibleTrees = getPerimiterTrees(mapSize) + internalVisibleTrees
    print(totalVisibleTrees)


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