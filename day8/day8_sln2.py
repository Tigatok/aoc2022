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

    treesToSearch = []
    highestScenicScore = 0
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

                # Up
                if (nXCount >= 0):
                    checkTree = int(coordinates[nXCount][y])
                    upTrees.append(int(checkTree))

                # Right
                if (yCount) < len(coordinates[y]):
                    checkTree = int(coordinates[x][yCount])
                    rightTrees.append(int(checkTree))

                # Down
                if (xCount) < len(coordinates[x]):
                    # Increment right away or else we will be on the same tree...
                    checkTree = int(coordinates[xCount][y])
                    downTrees.append(int(checkTree))

                # Left        
                if (nYCount >= 0):
                    checkTree = int(coordinates[x][nYCount])
                    leftTrees.append(int(checkTree))

                count += 1

            upViewScore = 0
            for upTree in upTrees:
                print("tree", tree, ">", upTree, tree > upTree)
                # The up tree blocks our view...
                if tree > int(upTree):
                    upViewScore += 1
                elif tree == int(upTree):
                    upViewScore += 1
                    break
                else:
                    upViewScore = +1
                    break

            rightViewScore = 0
            for rightTree in rightTrees:
                # The up tree blocks our view...
                if tree > int(rightTree):
                    rightViewScore += 1
                elif tree == int(rightTree):
                    rightViewScore += 1
                    break
                else:
                    rightViewScore += 1
                    break

            downViewScore = 0
            for downTree in downTrees:
                # The up tree blocks our view...
                if tree > int(downTree):
                    downViewScore += 1
                elif tree == int(downTree):
                    downViewScore += 1
                    break
                else:
                    downViewScore += 1
                    break
                        
            leftViewScore = 0
            for leftTree in leftTrees:
                # The up tree blocks our view...
                if tree > int(leftTree):
                    leftViewScore += 1
                elif tree == int(leftTree):
                    leftViewScore += 1
                    break
                else:
                    leftViewScore = +1
                    break
            print("Up view score for", tree, "is", upViewScore)
            print("Right view score for", tree, "is", rightViewScore)
            print("Down view score for", tree, "is", downViewScore)
            print("Left view score for", tree, "is", leftViewScore)
            
            scenicScore = upViewScore*rightViewScore*downViewScore*leftViewScore
            if scenicScore > highestScenicScore:
                highestScenicScore = scenicScore
            print("total view score for", tree, "is", upViewScore*rightViewScore*downViewScore*leftViewScore)
            print()
    print("Highest scenic score is", highestScenicScore)

if __name__ == "__main__":
    main()