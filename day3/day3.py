day3 = open("./day3.txt", "r")
day3 = day3.read()

priorityMap = '0abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWXYZ';
priorityMap = [*priorityMap]
print(priorityMap)
sumOfPriority = 0

rucksacks = day3.split("\n");
for rucksack in rucksacks: 
    firstCompartment, secondCompartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    charactersInFirst = [*firstCompartment]
    for character in charactersInFirst:
        priority = 0
        # Find the common item.
        if(character in secondCompartment):
            sumOfPriority = sumOfPriority + priorityMap.index(character);
            break;
print(sumOfPriority)