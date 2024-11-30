import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

# 100 octopuses in a 10x10 grid
def parse(puzzle_input):
    # parse the input
    return [[l for l in line] for line in puzzle_input.split()]

def adjacentcy(x, y):
    ret = []
    for i in [-1,0, 1]:
        for j in [-1,0,1]:
            ret.append([x+i,y+j])
    return [r for r in ret if 0 <= r[0] < 10 and 0 <=r[1] < 10]

def energize(grid):
    for i in range(0,10):
        for j in range(0,10):
            grid[i][j] = grid[i][j] + 1

def flash(grid):
    flashed = True
    while flashed:
        flashed = False
        for i in range(1,10):
            for j in range(1,10):
                if grid[i][j] >= 9:
                    flashed = True
                    for a in adjacentcy(grid[i][j]):
                        grid[a[0]][a[1]] = grid[a[0]][a[1]] + 1

def part1(parsed):
    print(parsed)
    print(adjacentcy(9,9))
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