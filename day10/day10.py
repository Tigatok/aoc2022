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
    sum = 0
    sum += cycles[19]['x'] * 20
    sum += cycles[59]['x'] * 60
    sum += cycles[99]['x'] * 100
    sum += cycles[139]['x'] * 140
    sum += cycles[179]['x'] * 180
    sum += cycles[219]['x'] * 220
    print(sum)

    for cycle in range(len(cycles)):
        print(f'cycle {cycle} is {cycles[cycle]}')
if __name__ == "__main__":
    main()