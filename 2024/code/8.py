from math import sqrt
import pathlib
import sys

SAMPLE_ANSWER_1 = 14
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    grid = {}
    puzzle_input = [[l for l in line.split()] for line in puzzle_input.splitlines()]
    bounds =(len(puzzle_input), len(puzzle_input[0]))
    for i in range(0, bounds[0]):
        for j in range(0, bounds[1]):
            if puzzle_input[i][j] != '.':
                temp = grid.get(puzzle_input[i][j], set())
                temp.add(puzzle_input[i][j])
                grid.update({puzzle_input[i][j]:temp)})
    return grid, bounds


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        # sqrt((x1-x2)^2+(y1-y2)^2)
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

def find_antinodes(points, bounds):
    pass

def anti_nodes(a,b):
    pass

def part1(parsed):
    print(parsed)
    grid, bounds = parsed
    return parsed

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
