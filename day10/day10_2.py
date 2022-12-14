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
    pixels = []
    rows =[]
    rowString = ''
    sprite = {
        'position': 1
    }
    spriteImage = '###'
    
    pixel = '.'
    # Cycles is 240 items.
    # Every 40 items, we want to break a new row.
    for i in range(len(cycles)):
        x = cycles[i]['x']
        # Break every 40 rows.
        if i > 0 and i % 40 == 0:
            rows.append(rowString)
            rowString = ''
        # Default the pixel to '.'
        pixel = '.'
        # print(cycles[i])
        print(i)
        # This is debugging...
        if i == sprite['position'] or i == sprite['position']-1 or i == sprite['position'] + 1:
            pixel = '#'
        rowString += pixel
        sprite['position'] = x
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()