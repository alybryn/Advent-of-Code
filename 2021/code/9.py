import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    ret = {}
    lines = puzzle_input.split()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            ret.update({(i, j): int(lines[i][j])})
    return ret

def adjacent(x, y):
    matrix = [(0,1), (0,-1), (1,0), (-1,0)]
    return [(x + m[0], y + m[1]) for m in matrix]

def part1(parsed):
    # find low points
    low_points = []
    for k in parsed.keys():
        height = parsed.get(k)
        lowest = True
        for xy in adjacent(k[0], k[1]):
            if parsed.get(xy, 10) < height:
                lowest = False
        if lowest:
            low_points.append(k)
    low_points_values = [parsed.get(l) for l in low_points]
    # sum low points + len(lowpoints)
    return sum(low_points_values) + len(low_points)

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