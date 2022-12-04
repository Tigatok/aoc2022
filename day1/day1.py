day1 = open("./day1.txt", "r")
day1 = day1.read()
elvesCaloriesList = day1.split('\n\n')
print(elvesCaloriesList)
sumOfEachElf = []
for elvesCalories in elvesCaloriesList:
    calories = elvesCalories.split('\n')
    calorieCount = 0
    for calorie in calories:
        calorieCount = calorieCount + int(calorie);
    sumOfEachElf.append(calorieCount);
    sumOfEachElf.sort(reverse=True)
firstThree = sum(sumOfEachElf[0:3])
print(firstThree);