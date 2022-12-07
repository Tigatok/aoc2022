# if it starts with a $ its a command
# if it starts with a dir its a directory
# if it stars with a number its a file

# A file has 3 parts, size, name and extension

# There are 2 commands, ls and cd

# ls lists all items within the current directory
# ls has no arguments

# cd changes the current directory into a new directory
# cd has 3 arguments:
#   - dirname - the directory name to change the current directory
#   - .. - go back one directory
#   - / - switch the current directory to the outer most directory



# For every line, it is either a command or an output.
# We need to track which directory we are in.

# Determine the total size of each directory (and their directories...)

# Find all directories with a total size of <= 100000

# Initial thoughts are to just search for all instances of ls command. Thi is not reliable because a cd .. and then an ls won't tell us what we are in.

# We know, currently, that we are going to need to know what directory we are in. We should solve for the logic of the CD command.

# What we need to do is read all of the output for an LS and update a map with those.
# So if the command is ls, set reading flag to true, and for every line, dont do normal logic until
# the read command is false (another command is on the line.)
def main():
    day7 = open("./day7.txt", "r")
    day7 = day7.read()
    solutionOne(day7)

def solutionOne(input):
    # Track previous in case we use ..
    parentDirectories = []
    currentDirectoryFiles = {}
    currentDirectory = '/'
    # Get input output lines.
    io = input.split('\n');
    for ioLine in io:
        lineParts = ioLine.split(' ')

        # If the line starts with $ it's a command.
        # We only care about the CD command, as ls provides nothing useful for us.
        if lineParts[0] == '$':
            # A command must be after a $.
            command = lineParts[1]
            # Change directory command.
            if command == 'cd':
                # If we are to move to previous, set current to previous.
                if lineParts[2] == '..':
                    currentDirectory = parentDirectories.pop()
                # If they change to /, there are no more parentDirectories.
                elif lineParts[2] == '/':
                    currentDirectory = '/'
                    parentDirectories = []
                else:
                    parentDirectories.append(currentDirectory)
                    currentDirectory = lineParts[2]
                    # # Else it is an output.
        # If its not a command, its an output from the ls.
        else:
            currentDirectoryFiles.update({'directory': currentDirectory, 'files': currentDirectoryFiles})
    assert currentDirectory == 'd'
    assert parentDirectories == ['/']
    # totalSize = 0
    # for currentDirectoryFile in currentDirectoryFiles:
    #     totalSize = totalSize + int(currentDirectoryFile[0])
    # assert totalSize == 24933642

if __name__ == "__main__":
    main()