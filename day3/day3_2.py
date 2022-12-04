day3 = open("./day3_2.txt", "r")
day3 = day3.read()

priorityMap = '0abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWXYZ';
priorityMap = [*priorityMap]
sumOfPriority = 0

lines = day3.split("\n")
groups = []
group = []
i = 0
for line in lines:
    i = i + 1
    group.append(line)  
    if i % 3 == 0:
        groups.append(group)
        group = []

sharedLetters = []
for group in groups:
    smallestRucksack = group[0]
    if len(smallestRucksack) > len(group[1]):
        smallestRucksack = group[1]
    if len(smallestRucksack) > len(group[2]):
        smallestRucksack = group[2]
    print(smallestRucksack);

    lettersInSmallest = [*smallestRucksack]
    for letter in lettersInSmallest:
        if letter in group[0] and letter in group[1] and letter in group[2]:
            sharedLetters.append(letter)
            break;

for sharedLetter in sharedLetters:
    sumOfPriority = sumOfPriority + priorityMap.index(sharedLetter);

print(sumOfPriority)