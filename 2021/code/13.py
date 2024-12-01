import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    dots, instructions = puzzle_input.split('\n\n')
    for dot in dots.split():
def findExtremes(grid):
    maxX = 0
    maxY = 0
    for g in grid:
        if g[0] > maxX:
            maxX = g[0]
        if g[1] > maxY:
            maxY = g[1]
    return (maxX,maxY)

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