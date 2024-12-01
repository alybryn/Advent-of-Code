import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    dots, instructions = puzzle_input.split('\n\n')
    grid = set()
    for dot in dots.split():
        x, y = dot.split(',')
        grid.add((int(x),int(y)))
    instructions = [i.strip('fold along ') for i in instructions.split('\n')]
    return (grid, instructions)

def fold(grid, instruction):
    xy, num = instruction.split('=')
    num  = int(num)
    newGrid = set()
    if xy == 'x':
        for dot in grid:
            if dot[0] < num:
                newGrid.add(dot)
            else:
                newGrid.add((dot[0]-num,dot[1]))
    if xy == 'y':
        for dot in grid:
            if dot[1] < num:
                newGrid.add(dot)
            else:
                newGrid.add((dot[0],dot[1]-num))

def findExtremes(grid):
    maxX = 0
    maxY = 0
    for g in grid:
        if g[0] > maxX:
            maxX = g[0]
        if g[1] > maxY:
            maxY = g[1]
    return (maxX,maxY)

def printGrid(grid):
    (maxX, maxY) = findExtremes(grid)
    maxX += 1
    maxY += 1
    pr = ''
    for y in range(0,maxY):
        for x in range(0,maxX):
            if (x,y) in grid:
                pr += '#'
            else:
                pr += '.'
        pr += '\n'
    print(pr)

def part1(parsed):
    grid, instructions = parsed
    gridCopy = grid.copy()
    fold(gridCopy, instructions[0])
    print(parsed)
    return 0

def part2(parsed):
    grid, instructions = parsed
    printGrid(grid)
    for i in instructions:
        fold(grid, i)
        printGrid(grid)
    return 0

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}")
        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))