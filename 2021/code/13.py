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
    print(parsed)
    return 0

def part2(parsed):
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