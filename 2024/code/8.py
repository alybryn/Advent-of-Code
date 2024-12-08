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

def find_antinodes(points):
    ret = []
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            ret += antinodes(p1, p2)
    return ret

def antinodes(p1, p2):
    v1 = Vector(p1.x - p2.x, p1.y - p2.y)
    v2 = Vector(v1.dx*-1, v1.dy*-1)
    return [Point(p1.x + v1.dx, p1.y + v1.dy),Point(p2.x+v2.dx,p2.y+v2.dy)]

def prune_to_bounds(points, bounds):
    return [p for p in points if 0 <= p.x < bounds[0] and 0 <= p.y < bounds[1]]

def part1(parsed):
    # print(parsed)
    grid, bounds = parsed
    antinodes = []
    for points in grid.values():
        antinodes += find_antinodes(points)
    antinodes = set(prune_to_bounds(antinodes, bounds))
    return len(antinodes)

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
