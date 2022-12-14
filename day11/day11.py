import math

monkeys = []

def main():
    inputFile = open("./input_e.txt", "r")
    inputFile = inputFile.read()
    solution(inputFile)

def solution(inputFile):
    monkey0 = Monkey(0, [57,58], 'old * 19', 7, [2,3])
    monkey1 = Monkey(1, [66,52,59,79,94,73], 'old + 1', 19, [4,6])
    monkey2 = Monkey(2, [80], 'old + 6', 5, [7,5])
    monkey3 = Monkey(3, [82,81,68,66,71,83,75,97], 'old + 5', 11, [5,2])
    monkey4 = Monkey(4, [55,52,67,70,69,94,90], 'old * old', 17, [0,3])
    monkey5 = Monkey(5, [69,85,89,91], 'old + 7', 13, [1,7])
    monkey6 = Monkey(6, [75,53,73,52,75], 'old * 7', 2, [0,4])
    monkey7 = Monkey(7, [94,60,79], 'old + 2', 3, [1,6])
    monkeys.append(monkey0)
    monkeys.append(monkey1)
    monkeys.append(monkey2)
    monkeys.append(monkey3)
    monkeys.append(monkey4)
    monkeys.append(monkey5)
    monkeys.append(monkey6)
    monkeys.append(monkey7)
    
    for i in range(20):
        for monkey in monkeys:
            monkey.inspectItems()
            newMonkeys = monkey.testItems()
            for newMonkey in newMonkeys:
                monkeys[newMonkey['id']].startingItems.append(newMonkey['itemId'])
    
    topMonkeys = []
    for monkey in monkeys:
        print("Monkey", monkey.id, "has", monkey.getItems(), "has inspected", monkey.getInspectedItemCount())
        topMonkeys.append(monkey.getInspectedItemCount())
        print()
    topMonkeys.sort()
    print(topMonkeys)
    top1 = topMonkeys.pop()
    top2 = topMonkeys.pop()
    print(top1*top2)
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
        self.inspectedItemCount = 0
    
    
    def getInspectedItemCount(self):
        return self.inspectedItemCount
    
    def inspectItems(self):
        for item in range(len(self.startingItems)):
            self.inspectedItemCount += 1
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