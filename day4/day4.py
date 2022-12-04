day4 = open("./day4.txt", "r")
day4 = day4.read()

sections = day4.split("\n");
sortedPairs = []
totalCoveredPairCount = 0
coveredPairCount = 0
for section in sections:
    pair = section.split(",")

    firstPairNumbers = pair[0].split('-')
    secondPairNumbers = pair[1].split('-')
    firstPairFirstNumber = int(firstPairNumbers[0])
    firstPairSecondNumber = int(firstPairNumbers[1]) 
    secondPairFirstNumber = int(secondPairNumbers[0])
    secondPairSecondNumber = int(secondPairNumbers[1])

    if (firstPairFirstNumber <= secondPairFirstNumber and firstPairSecondNumber >= secondPairSecondNumber) or (secondPairFirstNumber <= firstPairFirstNumber and secondPairSecondNumber >= firstPairSecondNumber):
        print(pair)
        totalCoveredPairCount = totalCoveredPairCount + 1;
    else:
        print(pair)

    if ((firstPairFirstNumber <= secondPairFirstNumber and firstPairSecondNumber >= secondPairFirstNumber) or (secondPairFirstNumber <= firstPairFirstNumber and secondPairSecondNumber >= firstPairFirstNumber)):
      coveredPairCount = coveredPairCount + 1;
      print(pair)
print(totalCoveredPairCount)
print(coveredPairCount)