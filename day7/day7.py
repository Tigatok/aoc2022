from pathlib import Path
def main():
    day7 = open("./day7.txt", "r")
    day7 = day7.read()
    solutionOne(day7)

def solutionOne(input):
    # This is the command lines.
    consoleLines = input.split('\n')

    # Init the map.
    directoryFileMap = {
    }
    currentDirectory = '/'

    for consoleLine in consoleLines:
        lineParts = consoleLine.split(' ')
        # If the first part is numeric, its a file.
        # We already know the directory we are in, so lets add it to the map.
        if lineParts[0].isnumeric():
            size = int(lineParts[0])
            directoryFileMap[currentDirectory] += size 
        elif lineParts[0] == '$':
            command = lineParts[1]
            # "Change the directory"
            if (command == 'cd'):
                # Either .. or an argument, both of which are directories.
                newDirectory = lineParts[2]
                # We need to go backwards.
                if newDirectory == '..':
                    oldDirectory = currentDirectory
                    parentDirectory = str(Path(oldDirectory).parent)
                    if parentDirectory == '.':
                        parentDirectory = '/'
                    currentDirectory = parentDirectory
                else:
                    # If our current directory is root, our next directory must have the leading slash.
                    if currentDirectory == '/':
                        currentDirectory = f'/{newDirectory}'
                    # No longer in the root directory, so our next directory....
                    else:
                        currentDirectory = f'/{currentDirectory}/{newDirectory}'
                    # We need to do some dir cleaning...
                    dirNames = []
                    for currentDirectorySlash in currentDirectory.split('/'):
                        if (currentDirectorySlash != ''):
                            dirNames.append(currentDirectorySlash)
                    cleanedDirNames = '/'.join(dirNames)
                    currentDirectory = ''.join(('/', cleanedDirNames))
                    # While we are traversing, the first time we see a cd with a 
                    # directory we haven't been into yet, we will not have a record of it.
                    if currentDirectory not in directoryFileMap:
                        directoryFileMap[currentDirectory] = 0
    # Now we have everything we need.
    # We need to loop over everything.
    # We loop once to get everything, we loop again to total
    # all the items where the name matches.
    for directoryName, size in directoryFileMap.items():
        matchedDirectories = 0
        totalSize = 0
        for directoryNameCheck, sizeCheck in directoryFileMap.items():
            if directoryNameCheck.startswith(directoryName):
                matchedDirectories += 1
                totalSize += int(sizeCheck)
        if matchedDirectories > 1:
            directoryFileMap[directoryName] = totalSize

    totalSizeOne = 0
    ts = 0
    for directoryName, size in directoryFileMap.items():
        ts += int(size)
        if int(size) <= 100000:
            totalSizeOne += int(size)
    print(totalSizeOne)

    diskSpaceAvailable = 70000000
    neededSpace = 30000000
    # 42805968
    currentSpace = directoryFileMap['/']
    # 27194032
    currentUnusedSpace = diskSpaceAvailable - currentSpace
    # 2805968
    requiredSpace = neededSpace - currentUnusedSpace
    eligibleDeletions = {}
    for directoryName, size in directoryFileMap.items():
        if int(size) >= requiredSpace:
            eligibleDeletions[directoryName] = size
    print(min(eligibleDeletions.values()))

if __name__ == "__main__":
    main()