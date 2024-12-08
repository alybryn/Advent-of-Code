from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 14
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    grid = {}
    puzzle_input = [[l for l in line] for line in puzzle_input.splitlines()]
    bounds =(len(puzzle_input), len(puzzle_input[0]))
    for i in range(0, bounds[0]):
        for j in range(0, bounds[1]):
            if puzzle_input[i][j] != '.':
                temp = grid.get(puzzle_input[i][j], set())
                temp.add(Point(i, j))
                grid.update({puzzle_input[i][j]:temp})
    return grid, bounds

Point = namedtuple('Point', ['x','y'])
Vector = namedtuple('Vector', ['dx','dy'])

def find_dist_antinodes(points, bounds):
    ret = []
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            p3 = dist_antinode(p1,p2)
            if is_in_bounds(p3, bounds):
                ret.append(p3)
    return ret

def dist_antinode(p1, p2):
    v = Vector(p1.x - p2.x, p1.y - p2.y)
    return Point(p1.x + v.dx, p1.y + v.dy)

def is_in_bounds(point, bounds):
    return 0 <= point.x < bounds[0] and 0 <= point.y < bounds[1]


def part1(parsed):
    # print(parsed)
    grid, bounds = parsed
    antinodes = []
    for points in grid.values():
        antinodes += find_dist_antinodes(points, bounds)
    return len(set(antinodes))

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
