import copy
def main():
    inputFile = open("./input_e.txt", "r")
    inputFile = inputFile.read()
    solution(inputFile)

def solution(inputFile):
    instructions = inputFile.split("\n")
    x = 1
    cycles = []
    cycles.append({'x': 1})
    for i in range(len(instructions)):
        instruction = instructions[i]
        print()
        print(f"Cycle {len(cycles)}, instruction: {instruction}")
        if instruction == 'noop':
            cycles.append({
                'x': x,
                'in': 'noop'
            })
        else:
            amount = int(instruction.split(' ')[1])
            cycles.append({
                'x': x,
                'in': amount
            })
            x += amount
            cycles.append({
                'x': x,
                'in': amount
            })

    # Would be 0, but x = 1.
    spritePosition = 1
    rows = []
    rowString = ''
    for i in range(len(cycles)):
        print(cycles[i])
        if i > 0 and i % 40 == 0:
            rows.append(rowString)
            rowString = ''
        rowString += '.'
    print (rows)
if __name__ == "__main__":
    main()