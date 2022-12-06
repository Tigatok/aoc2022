def main():
    day6 = open("./day6.txt", "r")
    day6 = day6.read()
    print(readMessage(day6, 4))
    print(readMessage(day6, 14))

def checkUnique(st):
    return len(set(st)) == len(st)

def readMessage(string, cap):
    totalString = ''
    index = 0
    while index <= len(string):
        totalString = totalString + string[index]
        chunk = totalString[index-cap:index]
        if len(chunk) >= cap and checkUnique(chunk):
            return index
        index = index + 1

if __name__ == "__main__":
    main()