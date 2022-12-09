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
                tree = coordinates[x][y]
                treeRight = coordinates[x][y+1]
                treeLeft = coordinates[x][y-1]
                treeUp = coordinates[x-1][y]
                treeDown = coordinates[x+1][y]
                if (
                    tree >= treeUp and
                    tree >= treeRight and
                    tree >= treeDown and
                    tree >= treeLeft
                    ):
                        print(coordinates[x][y])
                        internalVisibleTrees += 1
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