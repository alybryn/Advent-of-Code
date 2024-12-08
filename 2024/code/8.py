from math import sqrt
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


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # just return a vector... or two
    def dist(self, other):
        vs = (self.x - other.x, self.y - other.y)
        vo = (vs[0] * -1, vs[1] * -1)
        return (vs, vo)
    
    def add(self, vector):
        return Point(self.x + vector[0], self.y + vector[1])

    def antinodes(self, other):
        vs, vo = self.dist(other)
        return [self.add(vs), other.add(vo)]
        return [(self.x + vs[0], self.y + vs[1]), (other.x + vo[0], other.y + vo[1])]

    def __repr__(self):
        return f"({self.x}, {self.y})"

def find_antinodes(points):
    ret = []
    for p in points:
        for p2 in points:
            if p == p2:
                continue
            ret += p.antinodes(p2)
    # for i in range(0, len(points)):
    #     for j in range(i+1, len(points)):
    #         if i==j:
    #             continue
    #         ret += points[i].antinodes(points[i+1])
    return ret

def prune_to_bounds(points, bounds):
    return [p for p in points if 0 <= p.x < bounds[0] and 0 <= p.y < bounds[1]]
    # ret = set()
    # for p in points:
        # if 0 <= p[0] < bounds[0] and 0 <= p[1] < bounds[1]:
            # ret.add(p)

def part1(parsed):
    print(parsed)
    grid, bounds = parsed
    antinodes = []
    for points in grid.values():
        antinodes += find_antinodes(points)
    antinodes = set(prune_to_bounds(antinodes, bounds))
    print(antinodes)
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
