import re
day5 = open("./day5.txt", "r")
day5 = day5.read()

# Board is the top half of the input.
pieces = day5.split('\n\n');
boardRows = pieces[0].split('\n');
instructions = pieces[1].split('\n')

# Get board letters without the columns numbers.
boardLetters = boardRows[0:len(boardRows)-1]

# Get the chunks containing letters, or nothing if empty.
letterChunks = []
for boardLetterRow in boardLetters:
    chunkArray = []
    # Chunk every 4 characters.
    scrubbed = [boardLetterRow[i:i+4] for i in range(0,len(boardLetterRow), 4)]
    for section in scrubbed:
        if section == '    ':
            chunkArray.append(section.replace('    ',''))
        else:
            chunkArray.append(" ".join(re.findall("[a-zA-Z]+", section)))
    letterChunks.append(chunkArray);

# Convert columns to int array.
boardColumns = boardRows.pop().split(' ')
boardColumns = [ item for item in boardColumns if item != '']
boardColumns = [int(item) for item in boardColumns]

# Build box layout.
boxLayout = []
for x in range(len(boardColumns)):
    rowArray = []
    for row in letterChunks:
        if (row[x] != ''):
            rowArray.append(row[x]);
    boxLayout.append(rowArray);

# Flipper over.
reverseBoxLayout = []
for x in range(len(boxLayout)):
    reverse = boxLayout[x][::-1]
    reverseBoxLayout.append(reverse);

def moveBoxes(amount, fromColumn, toColumn, keepFormat):
    fromColumn = fromColumn - 1
    toColumn = toColumn - 1
    for index in range(len(reverseBoxLayout)):
        if (index == fromColumn):
            if reverseBoxLayout[index]:
                movedBoxes = []
                if (keepFormat):
                    for x in range(amount):
                        movedBox = reverseBoxLayout[index].pop();
                        movedBoxes.append(movedBox)
                    movedBoxes = movedBoxes[::-1]
                    for movedBox in movedBoxes:
                        reverseBoxLayout[toColumn].append(movedBox);
                else:
                    for x in range(amount):
                        movedBox = reverseBoxLayout[index].pop();
                        reverseBoxLayout[toColumn].append(movedBox);

for instruction in instructions:
    ints = re.findall(r'\d+', instruction);
    amount = int(ints[0])
    fromColumn = int(ints[1])
    toColumn = int(ints[2])
    moveBoxes(amount, fromColumn, toColumn,True) 
topBoxes = ''
for boxes in reverseBoxLayout:
    topBoxes = topBoxes+boxes.pop()
print(topBoxes)