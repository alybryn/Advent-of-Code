import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

GRID_SIZE = 5

# 100 octopuses in a 10x10 grid
def parse(puzzle_input):
    # parse the input
    return [[int(l) for l in line] for line in puzzle_input.split()]

def gridPrint(grid):
    pr = ''
    for i in grid:
        for j in i:
            pr += str(j)
        pr += '\n'
    print(pr)

def adjacentcy(x, y):
    ret = []
    for i in [-1,0, 1]:
        for j in [-1,0,1]:
            ret.append([x+i,y+j])
    return [r for r in ret if 0 <= r[0] < GRID_SIZE and 0 <=r[1] < GRID_SIZE]

def energize(grid):
    for i in range(0,GRID_SIZE):
        for j in range(0,GRID_SIZE):
            grid[i][j] = grid[i][j] + 1

def flash(grid):
    flashed = True
    while flashed:
        flashed = False
        for i in range(0,GRID_SIZE):
            for j in range(0,GRID_SIZE):
                if grid[i][j] >= 9:
                    flashed = True
                    grid[i][j] = 0
                    for a in adjacentcy(i,j):
                        if grid[a[0]][a[1]] != 0:
                            grid[a[0]][a[1]] = grid[a[0]][a[1]] + 1

def step(grid):
    energize(grid)
    flash(grid)

def part1(parsed):
    gridPrint(parsed)
    step(parsed)
    step(parsed)
    gridPrint(parsed)
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