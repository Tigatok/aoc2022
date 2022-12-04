day2 = open("./day2.txt", "r")
day2 = day2.read()
def getValue(move):
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    elif move == "Z":
        return 3

# X lose, Y draw, Z win
def getOutcomeValue(hand1, hand2):
    # rock
    if hand1 == "A": # rock
        if hand2 == "X":
            return 3;
        elif hand2 == "Y":
            return 6;
        elif hand2 == "Z":
            return 0;
    elif hand1 == "B": # paper
        if hand2 == "X":
            return 0;
        elif hand2 == "Y":
            return 3;
        elif hand2 == "Z":
            return 6;
    elif hand1 == "C": # scissors
        if hand2 == "X":
            return 6
        elif hand2 == "Y":
            return 0;
        elif hand2 == "Z":
            return 3;

def getDecidedOutcomeValue(hand1, hand2):
  if hand1 == "A": # Rock
    if hand2 == "X": # We must lose.
      return getOutcomeValue(hand1, "Z") + getValue("Z")
    elif hand2 == "Y": # We must draw.
        return getOutcomeValue(hand1, "X") + getValue("X")
    elif hand2 == "Z": # We must win.
        return getOutcomeValue(hand1, "Y") + getValue("Y")
  elif hand1 == "B": # Paper
    if hand2 == "X": # We must lose.
        return getOutcomeValue(hand1, "X") + getValue("X")
    elif hand2 == "Y": # We must draw.
        return getOutcomeValue(hand1, "Y") + getValue("Y")
    elif hand2 == "Z": # We must win.
        return getOutcomeValue(hand1, "Z") + getValue("Z")
  elif hand1 == "C": # Scissors
    if hand2 == "X": # We must lose.
        return getOutcomeValue(hand1, "Y") + getValue("Y")
    elif hand2 == "Y": # We must draw.
        return getOutcomeValue(hand1, "Z") + getValue("Z")
    elif hand2 == "Z": # We must win.
        return getOutcomeValue(hand1, "X") + getValue("X")


rounds = day2.split("\n");
total_outcome = 0;
for round in rounds:
    moves = round.split(" ")
    opp = moves[0]
    me = moves[1]
    total_outcome = total_outcome + getDecidedOutcomeValue(opp, me)
print(total_outcome);