day6 = open("./day6.txt", "r")
day6 = day6.read()

def checkUnique(st):
    return len(set(st)) == len(st)

totalString = ''
index = 0
while index <= len(day6):
    totalString = totalString + day6[index]
    chunk = totalString[index-14:index]
    if len(chunk) >= 14 and checkUnique(chunk):
        break;
    index = index + 1
print(index)