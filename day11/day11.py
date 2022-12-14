import math

monkeys = []

def main():
    inputFile = open("./input_e.txt", "r")
    inputFile = inputFile.read()
    solution(inputFile)

def solution(inputFile):
    monkey0 = Monkey(0, [79,98], 'old * 19', 23, [2,3])
    monkey1 = Monkey(1, [54,65,75,74], 'old + 6', 19, [2,0])
    monkey2 = Monkey(2, [79, 60, 97], 'old * old', 13, [1,3])
    monkey3 = Monkey(3, [74], 'old + 3', 17, [0,1])
    monkeys.append(monkey0)
    monkeys.append(monkey1)
    monkeys.append(monkey2)
    monkeys.append(monkey3)
    
    for monkey in monkeys:
        monkey.inspectItems()
        newMonkeys = monkey.testItems()
        for newMonkey in newMonkeys:
            monkeys[newMonkey['id']].startingItems.append(newMonkey['itemId'])
    
    for monkey in monkeys:
        print("Monkey", monkey.id, "has", monkey.getItems())
        print()
    # monkey0.inspectItems()
    # newMonkeys = monkey0.testItems()
    # print(newMonkeys)

def doOperation(operator, number1, number2):
    print("Do Op", number1, operator, number2)
    number1 = int(number1)
    number2 = int(number2)
    if operator == '/':
        return number1 / number2
    elif operator == '+':
        return number1+number2 
    elif operator == '*':
        return number1 * number2
    else:
        return number1 - number2

class Monkey:
    def __init__(self, id, startingItems, operation, test, conditions):
        self.id = id
        self.startingItems = startingItems
        self.operation = operation
        self.test = test
        self.conditions = conditions
    
    
    def inspectItems(self):
        for item in range(len(self.startingItems)):
            newWorryLevel = self.inspectItem(self.startingItems[item], self.operation)
            print("New Worry Level:", newWorryLevel)

    def addItems(self, itemId):
        print("Adding item", itemId, "to monkey", self.id)
        self.startingItems.append(itemId)

    # Changes worry level of the item
    def inspectItem(self, itemId, operation):
        self.operationParts = operation.split(' ')
        print(self.operationParts)
        print(self.startingItems.index(itemId))
        
        oldWorryLevel = self.startingItems[self.startingItems.index(itemId)]
        newWorryLevel = 0
        # Use the old value of.
        if self.operationParts[0] == 'old':
            operator = self.operationParts[1]
            if self.operationParts[2] == 'old':
                newWorryLevel = doOperation(operator, oldWorryLevel, oldWorryLevel)
            else:
                newWorryLevel = doOperation(operator, oldWorryLevel, self.operationParts[2])

        # Get bored...
        newWorryLevel /= 3
        newWorryLevel = math.floor(newWorryLevel)
        self.setWorryLevel(itemId, newWorryLevel)
        return newWorryLevel

    def testItems(self):
        newMonkeys = []
        for item in self.startingItems:
            newMonkey = {}
            if item % self.test == 0:
                newMonkey['id'] = self.conditions[0]
            else:
                newMonkey['id'] = self.conditions[1]
            newMonkey['itemId'] = item 
            newMonkeys.append(newMonkey)
        self.startingItems = []
        return newMonkeys


    def setWorryLevel(self, itemId, worryLevel):
        self.startingItems[self.startingItems.index(itemId)] = worryLevel

    def getItems(self):
        return self.startingItems
        

if __name__ == "__main__":
    main()